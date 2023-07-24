#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
Using "https://jsonplaceholder.typicode.com/"
Returns information about his/her TODO list progress
"""
import csv
import requests
from sys import argv


def gather_data_to_csv():
    """Fetches data of employees and their todo tasks"""

    # Make a GET request to fetch data of all users
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
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export to csv"""
    # Create a new CSV file with the name "<employee_id>.csv" in write mode
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        # Create a CSV writer object with quoting all fields
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
        # Write each task's data to the CSV file as a row
        for task in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": task[0],
                             "TASK_TITLE": task[1]})


if __name__ == "__main__":
    # Execute the gather_data_to_csv() function when the script is run
    gather_data_to_csv()
