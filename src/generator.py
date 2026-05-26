import secrets
import os
import uuid
import hashlib


ALGORITHMS = ["secrets.token_hex", "os.urandom + sha256", "UUID4"]


def generate_password(algorithm: str = "secrets.token_hex", length: int = 32) -> str:
    if algorithm == "secrets.token_hex":
        return secrets.token_hex(length // 2)[:length]

    elif algorithm == "os.urandom + sha256":
        raw = os.urandom(64)
        return hashlib.sha256(raw).hexdigest()[:length]

    elif algorithm == "UUID4":
        base = uuid.uuid4().hex + uuid.uuid4().hex
        return base[:length]

    raise ValueError(f"Unknown algorithm: {algorithm}")
