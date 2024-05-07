def cast_dict(s: str | dict) -> dict:
    """a@1,b@2"""
    if not isinstance(s, str):
        return s
    return {_[0]: _[1] for _ in (i.split("@") for i in s.strip(',').split(","))}
