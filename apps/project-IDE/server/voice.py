"""Voice input for the page's request boxes: a recording in, its text out, through Groq.

The page records up to five minutes in the browser and posts the audio to api/voice.
This module sends it to Groq's speech-to-text API, trying the models listed in
server.config.json ("voice.models") in order. A model that answers with a rate limit is
skipped until its wait is over; an error moves on to the next model. The key is read from
the keys file on this machine (secrets.keys lists GROQ_API_KEY) and never leaves the server.
Standard library only.
"""
import json
import threading
import time
import urllib.error
import urllib.request
import uuid

DEFAULTS = {
    "url": "https://api.groq.com/openai/v1/audio/transcriptions",
    "models": ["whisper-large-v3-turbo", "whisper-large-v3"],
    "key": "GROQ_API_KEY",
    "max_seconds": 300,
    "max_bytes": 25 * 1024 * 1024,   # Groq's limit for a direct upload on the free tier
    "language": None,                # None: Groq detects the language
    "timeout_s": 120,
}
EXT = {"audio/webm": "webm", "audio/ogg": "ogg", "audio/mp4": "m4a", "audio/mpeg": "mp3", "audio/wav": "wav", "audio/x-wav": "wav"}


class Voice:
    def __init__(self, cfg, secrets):
        self.cfg = {**DEFAULTS, **(cfg.get("voice") or {})}
        self.key = secrets.get(self.cfg["key"])
        self.cooldown = {}   # model -> time before which it is skipped
        self.lock = threading.Lock()

    @property
    def available(self):
        return bool(self.key and self.cfg["models"])

    def transcribe(self, audio, ctype):
        """Returns {"text", "model"}; raises ValueError for a bad recording, RuntimeError when every model failed."""
        if not self.available:
            raise RuntimeError(f"voice is off: {self.cfg['key']} is not in the keys file")
        if not audio:
            raise ValueError("empty recording")
        if len(audio) > self.cfg["max_bytes"]:
            raise ValueError("recording too large")
        ctype = (ctype or "audio/webm").split(";")[0].strip()
        now, errors = time.time(), []
        with self.lock:
            ready = [m for m in self.cfg["models"] if self.cooldown.get(m, 0) <= now]
        # every model resting: try the one whose wait ends first rather than refuse
        order = ready or sorted(self.cfg["models"], key=lambda m: self.cooldown.get(m, 0))[:1]
        for model in order:
            try:
                return {"text": self._call(model, audio, ctype), "model": model}
            except urllib.error.HTTPError as e:
                wait = _retry_after(e) if e.code == 429 else (60 if e.code >= 500 else 0)
                if wait:
                    with self.lock:
                        self.cooldown[model] = time.time() + wait
                errors.append(f"{model}: {e.code} {_message(e)}")
            except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
                errors.append(f"{model}: {e}")
        raise RuntimeError("transcription failed: " + "; ".join(errors))

    def _call(self, model, audio, ctype):
        fields = {"model": model, "response_format": "json", "temperature": "0"}
        if self.cfg.get("language"):
            fields["language"] = self.cfg["language"]
        body, boundary = _multipart(fields, "recording." + EXT.get(ctype, "webm"), ctype, audio)
        req = urllib.request.Request(self.cfg["url"], data=body, method="POST", headers={
            "Authorization": "Bearer " + self.key,
            "Content-Type": "multipart/form-data; boundary=" + boundary,
            "User-Agent": "project-ide/1"})
        with urllib.request.urlopen(req, timeout=self.cfg["timeout_s"]) as r:
            return (json.loads(r.read() or b"{}").get("text") or "").strip()


def _multipart(fields, filename, ctype, data):
    b = uuid.uuid4().hex
    out = []
    for k, v in fields.items():
        out.append(f'--{b}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
    out.append(f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\nContent-Type: {ctype}\r\n\r\n'.encode())
    out += [data, f"\r\n--{b}--\r\n".encode()]
    return b"".join(out), b


def _retry_after(e):
    try:
        return max(5, min(3600, float(e.headers.get("retry-after") or 60)))
    except (TypeError, ValueError):
        return 60


def _message(e):
    try:
        return (json.loads(e.read() or b"{}").get("error") or {}).get("message", "")[:200]
    except Exception:
        return ""
