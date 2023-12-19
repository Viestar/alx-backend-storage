#!/usr/bin/env python3
"""
Module with function that returnsall students sorted by average score
"""


def top_students(mongo_collection):
    """
    Function uses an aggregate pipeline to calculate the average score
    of students and returns a sorted.
    Args:
        mongo_collection: pymongo collection object
    Returns: All students sorted by average score
    """
    pipeline = []
    return mongo_collection.find({"topics": {"$in": [topic]}})
