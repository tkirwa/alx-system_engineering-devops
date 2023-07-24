#!/usr/bin/python3
"""
Module 2-export_to_JSON
Using "https://jsonplaceholder.typicode.com/"
Exports information about his/her TODO list progress to JSON
"""
import json
import requests
from sys import argv


def export_to_json():
    """Fetches data of employees and their todo tasks"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)

    # Find the user with the given employee ID and get their username
    USERNAME = ""
    for i in users.json():
        if i.get("id") == int(argv[1]):
            USERNAME = i.get("username")
            break

    # Fetch all the TODO tasks associated with the given employee ID
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append({
                "task": t.get('title'),
                "completed": t.get('completed'),
                "username": USERNAME
            })

    """export to JSON"""
    # Create a new JSON file with the name "<employee_id>.json" in write mode
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as jsonfile:
        # Dump the list of tasks to the JSON file
        json.dump({argv[1]: TASK_STATUS_TITLE}, jsonfile)


if __name__ == "__main__":
    # Execute the export_to_json() function when the script is run
    export_to_json()
