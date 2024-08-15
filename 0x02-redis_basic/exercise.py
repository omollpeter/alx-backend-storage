#!/usr/bin/env python3
"""
Contains class definitions for Cache instance of Redis
"""


import redis
from typing import Union, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    A decorator to count all the 
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method_name = method.__qualname__
        self._redis.incr(method_name)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """
    Class Definition for Cache
    """

    def __init__(self) -> None:
        """Initializes Cache instance variables"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a key, store input data using the key in Redis server
        and returns the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    @count_calls
    def get(
            self, key: str, fn: Callable = None
        ) -> Union[bytes, str, int, float]:
        """
        Retrives a value with its requested format (bytes|str|int|flt)
        """
        value = self._redis.get(key)
        if fn:
            if value:
                return fn(value)
        return value
    
    @count_calls
    def get_str(self, key: str) -> Union[str, bytes]:
        """Returns string value of a particular key"""
        return self.get(key, str)

    @count_calls
    def get_int(self, key: str) -> Union[int, bytes]:
        """Returns integer value of a particular key"""
        return self.get(key, int)
