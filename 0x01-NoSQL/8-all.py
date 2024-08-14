#!/usr/bin/env python3
"""
This module contains a function that lists all documents in a collection
"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Returns a list of documents in mongo_collection
    """
    docs = mongo_collection.find()
    return docs
