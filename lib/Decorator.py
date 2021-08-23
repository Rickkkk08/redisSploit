import functools
import redis


def CatchPrivilegeException(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except redis.exceptions.ResponseError:
            print("Permission denied, not root!")

    return wrapper


def CatchConnectionException(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except redis.exceptions.ConnectionError as e:
            print(e)
        except redis.exceptions.TimeoutError as e:
            print(e)
    return wrapper


def CatchKeyboardException(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            print("Canceled by user")

    return wrapper
