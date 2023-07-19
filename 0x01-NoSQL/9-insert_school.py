#!/usr/bin/env python3

"""
This module provides a function to insert a new document
in a MongoDB collection.
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the given MongoDB collection.

    Args:
        mongo_collection: The PyMongo collection object.
        **kwargs: Arbitrary keyword arguments representing the fields
        of the document.

    Returns:
        The newly inserted document.
    """
    document = kwargs
    result = mongo_collection.insert_one(document)
    return mongo_collection.find_one({'_id': result.inserted_id})


def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.

    Args:
        mongo_collection: The PyMongo collection object.

    Returns:
        A list of documents in the collection.
    """
    return [doc for doc in mongo_collection.find()]


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    school_collection = client.my_db.school

    # Insert new school and print details
    new_school = insert_school(school_collection,
                               name="UCSF", address="505 Parnassus Ave")
    print("New school created: [{}] {} {}".format(new_school.get('_id'), " \
          "new_school.get('name'), new_school.get('address', "")))

    # Print details for all schools in the collection
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), " \
              "school.get('address', "")))
