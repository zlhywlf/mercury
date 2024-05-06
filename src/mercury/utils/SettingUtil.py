def parse_dict(s: str) -> dict:
    """a:1,b:2"""
    return {_[0]: _[1] for _ in (i.split(":") for i in s.strip(',').split(","))}
