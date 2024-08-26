#!/usr/bin/env python3

"""
This script connects to a MongoDB instance and performs various queries on the 'nginx' collection
in the 'logs' database. It provides counts of:

1. Total number of documents in the collection.
2. Number of documents for each HTTP method (GET, POST, PUT, PATCH, DELETE).
3. Number of documents where the HTTP method is 'GET' and the path is '/status'.

It handles connection failures and prints an error message if the connection to MongoDB cannot be established.

Dependencies:
- pymongo: Python driver for MongoDB.

Usage:
Run this script directly to perform the queries and output the results to the console.
"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    """
    Connects to a MongoDB instance, retrieves data from the 'nginx' collection
    in the 'logs' database, and performs various counts:

    1. Prints the total number of documents in the collection.
    2. Prints the count of documents for each HTTP method (GET, POST, PUT, PATCH, DELETE).
    3. Prints the count of documents where the HTTP method is 'GET' and the path is '/status'.

    Handles connection failures and prints an error message if the connection cannot be established.
    """
    try:
        # Connect to MongoDB
        client = MongoClient()  # Connects to localhost:27017 by default
        db = client.logs  # Access the 'logs' database
        collection = db.nginx  # Access the 'nginx' collection
    except ConnectionFailure:
        print("Could not connect to MongoDB")
        return

    # Total number of documents
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count of each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of documents with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    """
    Entry point of the script. Calls the main function to execute the MongoDB queries 
    and display results.
    """
    main()