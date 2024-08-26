#!/usr/bin/env python3
"""11. Where can I learn Python? """


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic:
    -mongo_collection will be the pymongo collection object
    -topic (string) will be topic searched
    """

    list_of_school = mongo_collection.find({"topics": topic})
    return list_of_school