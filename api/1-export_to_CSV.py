#!/usr/bin/python3
"""API request for employee name and todos completed"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{url}/users/{sys.argv[1]}").json()
    todos = requests.get(f"{url}/todos", params={"userId": sys.argv[1]}).json()
    filename = f"{user['id']}.csv"

    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user["id"], user["username"],
                            str(todo["completed"]), todo["title"]])
