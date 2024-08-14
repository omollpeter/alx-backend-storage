#!/usr/bin/env python3
"""
Contains a function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return schools
