#!/usr/bin/python3
"""
Returns information about his/her TODO list progress for a
given employee ID using a REST API and exports the data to a CSV file.
"""
import csv
import requests
from sys import argv


def fetch_todo_list(employee_id):
    """Fetches employee's TODO list progress"""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()

        return user_data, todo_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None


def export_to_csv(employee_id, user_data, todo_data):
    """Exports TODO list progress to a CSV file"""
    if user_data is None or todo_data is None:
        return

    file_name = f'{employee_id}.csv'
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS',
                      'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todo_data:
            writer.writerow({
                'USER_ID': user_data['id'],
                'USERNAME': user_data['name'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = argv[1]
        user_data, todo_data = fetch_todo_list(employee_id)
        export_to_csv(employee_id, user_data, todo_data)
