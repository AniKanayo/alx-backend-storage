#!/usr/bin/env python3

"""
This module provides a function to list all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.

    Args:
        mongo_collection: The PyMongo collection object.

    Returns:
        A list of strings representing the documents in the collection.
        Each string contains the document's ID and its 'name' attribute.
        Returns an empty list if there are no documents in the collection.
    """
    documents = []
    for document in mongo_collection.find():
        document_str = f"[{document['_id']}] {document['name']}"
        documents.append(document_str)
    return documents

if __name__ == "__main__":
    # Test the function
    from pymongo import MongoClient

    # Connect to MongoDB
    client = MongoClient()
    db = client.my_database
    collection = db.my_collection

    # Insert some test documents
    collection.insert_many([
        {"name": "Holberton school"},
        {"name": "UCSD"}
    ])

    # Call the function and print the result
    result = list_all(collection)
    for document in result:
        print(document)
