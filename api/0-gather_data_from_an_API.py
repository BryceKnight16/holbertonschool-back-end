#!/usr/bin/python3
"""Script that shows the progress of a to do list"""
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user_todos = requests.get(f"{url}users/{sys.argv[1]}/todos").json()
    user_info = requests.get(f"{url}users/{sys.argv[1]}").json()

    total_todos = len(user_todos)
    completed_todos = 0
    for todo in user_todos:
        if todo.get("completed"):
            completed_todos += 1

    user_name = user_info.get("name")
    print(f"Employee {user_name} is done with "
          f"tasks({completed_todos}/{total_todos}):")

    for todo in user_todos:
        if todo.get("completed"):
            print(f"\t {todo['title']}")
