#!/usr/bin/env python3
"""
A function that inserts a new document in a collection
base on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Adds a new document to an existing collection
    Args:
        pymongo collection object: mongo_collection
        kwargs: a new document to be inserted

    Returns:
        New document id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
