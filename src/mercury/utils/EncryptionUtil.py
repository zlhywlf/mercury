import hashlib


def encrypt_by_md5(data: str, key: str) -> str:
    """"""
    return hashlib.md5(f"{data}{key}".encode("utf-8")).hexdigest()
