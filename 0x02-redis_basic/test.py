#!/usr/bin/env python3
"""
Redis' Hello world
"""


import redis

r = redis.Redis() # Central class of package

r.mset({"Kenya": "Nairobi", "Uganda": "Kampala"}) # Redis commands takes Python objects

print(r.get("Kenya").decode("utf-8")) # Bytes - Use .decode("utf-8") to get string

# Allowed keys are str, bytes, int and float