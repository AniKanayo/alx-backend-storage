#!/usr/bin/env python3
"""
This module provides a function to find and return 
the schools that have a specific topic in their topics list.
"""

from pymongo import MongoClient

def schools_by_topic(mongo_collection, topic):
    """
    Find and list schools having a specific topic.

    Args:
    mongo_collection: The PyMongo collection object.
    topic (str): The topic to look for.

    Returns: List of schools having the specific topic.
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return [school for school in schools]

# This script should not run when imported
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    # Find schools by topics and print them out
    specific_schools = schools_by_topic(school_collection, 'Python')
    for school in specific_schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'),
              school.get('topics', "")))
