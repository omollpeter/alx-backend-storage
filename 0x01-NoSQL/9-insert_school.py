#!/usr/bin/env python3
"""
This module contains a function that inserts a new document in a collection
based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection and returns its id
    """
    id_inserted = mongo_collection.insert_one(kwargs).inserted_id
    return id_inserted
