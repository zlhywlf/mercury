import functools


def authentication(func):
    """"""

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        rep = await func(*args, **kwargs)
        return rep

    return wrapper
