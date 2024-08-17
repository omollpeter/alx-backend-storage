#!/usr/bin/env python3
"""
This is a program to provide some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient

# Create a client for logs retrieval
client = MongoClient("mongodb://127.0.0.1:27017")

# Use the logs database
db = client.logs

# Initialize the Nginx collections
ngx_col = db.nginx

# Total log counts
total_logs = ngx_col.count_documents({})


def get_log_count_by_method(collection, method):
    """
    Returns the number of logs
    """
    count = collection.count_documents({"method": method})
    return count


def count_status_checks(collection):
    """
    Returns number of status checks
    """
    count = collection.count_documents({"method": "GET", "path": "/status"})
    return count


if __name__ == "__main__":
    print(f"{total_logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {get_log_count_by_method(ngx_col, method)}")
    print(f"{count_status_checks(ngx_col)} status checks")
    client.close()
