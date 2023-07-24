#!/usr/bin/python3
import requests
import sys


def gather_data_from_api(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)
        user_data = user_response.json()
        todo_data = todo_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    employee_name = user_data.get('name')
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    print(f"Employee {employee_name} is done with tasks({done_tasks}/"
          "{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"    {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data_from_api(employee_id)
