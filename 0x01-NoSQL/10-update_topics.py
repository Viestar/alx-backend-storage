#!/usr/bin/env python3
"""
Module with a function that updates all topics of a school document
 based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.
    Args:
        mongo_collection: pymongo collection object
        name(str): school name to update
        topics(str): list of topics
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
