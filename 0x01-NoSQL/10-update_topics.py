#!/usr/bin/env python3
"""
This module provides a function to update the topics of a school document 
in a MongoDB collection based on the school's name.
"""

from pymongo import MongoClient

def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document in a MongoDB
    collection based on the school's name.

    Args:
    mongo_collection: The PyMongo collection object.
    name (str): The name of the school.
    topics (list of str): The list of topics approached in the school.

    Returns: None
    """
    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})

# This script should not run when imported
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    # Update the topics for a specific school and print the updated documents
    update_topics(school_collection, 'Holberton school',
                 ['Sys admin', 'AI', 'Algorithm'])
    schools = school_collection.find()
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'),
              school.get('name'), school.get('topics', "")))
