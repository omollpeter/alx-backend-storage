#!/usr/bin/env python3
"""
This module contains a function that returns all students sorted by
average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    # mongo_collection.delete_many({})
    # students = mongo_collection.find()
    # for student in students:
    #     totalScore = 0
    #     for topic in student.get("topics"):
    #         totalScore += topic.get("score")
    #     averageScore = totalScore / len(student.get("topics"))
    #     mongo_collection.update_one(
    #         {"name": student.get("name")},
    #         {"$set": {"averageScore": averageScore}}
    #     )
    # return mongo_collection.find().sort({"averageScore": -1})
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
