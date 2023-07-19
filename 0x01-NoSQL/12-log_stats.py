#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient

# Connect to the MongoDB and access the logs collection in nginx database
client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

# Count and print the total number of logs
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Define the HTTP methods we're interested in
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("Methods:")
# For each method, count and print the number of logs with that method
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Count and print the number of documents where method is GET and path status
status_check = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check} status check")
