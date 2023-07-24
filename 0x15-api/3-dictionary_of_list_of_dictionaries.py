#!/usr/bin/python3
"""Script to export data in the JSON format."""
import json
import requests


def fetch_user_data():
    """Fetch user data from the API."""
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    users = response_users.json()
    todos = response_todos.json()

    return users, todos


def create_user_tasks_dict(users, todos):
    """Create a dictionary with user IDs as keys and their tasks as values."""
    user_tasks = {}
    for user in users:
        user_id = user['id']
        user_tasks[user_id] = []
        for todo in todos:
            if todo['userId'] == user_id:
                user_tasks[user_id].append({
                    'username': user['username'],
                    'task': todo['title'],
                    'completed': todo['completed']
                })
    return user_tasks


def export_to_json(user_tasks):
    """Export user tasks to JSON file."""
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == "__main__":
    users, todos = fetch_user_data()
    user_tasks = create_user_tasks_dict(users, todos)
    export_to_json(user_tasks)
