#!/usr/bin/env python3
"""
This is a program to provide some stats about Nginx logs stored in MongoDB
"""


from pymongo import MongoClient
import itertools


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


def count_and_sort_ips(collection):
    "Counts and returns top ten ips"
    entries = collection.find()
    ips = []
    for entry in entries:
        ips.append(entry.get("ip"))
    keys = set(ips)

    ips_count = {key: ips.count(key) for key in keys}
    sorted_ips = dict(sorted(ips_count.items(), key=lambda item: item[1], reverse=True))
    top_ten_ips = dict(itertools.islice(sorted_ips.items(), 10))
    return top_ten_ips

    # ipcount = {ip: collection.count_documents({"ip": ip}) for ip in ips}
    return ips

if __name__ == "__main__":
    print(f"{total_logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {get_log_count_by_method(ngx_col, method)}")
    print(f"{count_status_checks(ngx_col)} status checks")
    for key, value in count_and_sort_ips(ngx_col).items():
        print(f"\t{key}: {value}")
    client.close()
