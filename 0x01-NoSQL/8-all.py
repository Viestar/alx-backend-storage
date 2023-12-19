#!/usr/bin/env python3
"""
Module with a function that list all document in a collection
"""


def list_all(mongo_collection):
    """
    Returns a lists all documents in a collection or an empty list
    """
    return mongo_collection.find()
