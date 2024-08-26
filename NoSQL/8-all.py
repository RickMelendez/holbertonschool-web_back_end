#!/usr/bin/env python3
"""8. List all documents in Python"""

def list_all(mongo_collection):
    """
    function that lists all documents in a collection
    """

    documents = list(mongo_collection.find())

    return documents