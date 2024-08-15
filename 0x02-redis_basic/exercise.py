#!/usr/bin/env python3
"""
Contains class definitions for Cache instance of Redis
"""


import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    Class Definition for Cache
    """

    def __init__(self) -> None:
        """Initializes Cache instance variables"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a key, store input data using the key in Redis server
        and returns the key
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
