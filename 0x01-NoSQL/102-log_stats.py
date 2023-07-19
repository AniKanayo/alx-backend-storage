#!/usr/bin/env python3
"""
This script provides statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient

# Connect to the MongoDB and access logs collection in nginx database
client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

# Count and print the total number of logs
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

# Define the HTTP methods we're interested in
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("Methods:")
# For each method, count and print the number of logs with method
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

# Count and print the number of documents where method is GET ands
status_check = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check} status check")

# Determine and print the top 10 most present IPs
top_ips = collection.aggregate([
    {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])

print("IPs:")
for top_ip in list(top_ips):
    print(f"\t{top_ip['_id']}: {top_ip['count']}")
