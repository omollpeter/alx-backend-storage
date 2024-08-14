#!/usr/bin/env python3
"""
Contains a python func that changes(updates) all topics of a school
document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
