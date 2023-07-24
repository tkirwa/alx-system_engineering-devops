#!/usr/bin/python3
"""
returns information about his/her TODO list progress for a
given employee ID using a REST API
"""
import requests
from sys import argv


def get_todo():
    """returns employee's TODO list progress"""

    # Send a GET request to fetch user data for the given employee ID
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))

    # Send a GET request to fetch completed TODO list data for the employee ID
    r_todo_true = requests.get('https://jsonplaceholder.typicode.com/todos?'
                               'userId={}&&completed=true'.format(argv[1]))

    # Send a GET request to fetch uncompleted TODO list data for the
    #  employee ID
    r_todo_false = requests.get('https://jsonplaceholder.typicode.com/todos?'
                                'userId={}&&completed=false'.format(argv[1]))

    try:
        # Check if the API request was successful
        r_user.raise_for_status()
        r_todo_true.raise_for_status()
        r_todo_false.raise_for_status()

        # Parse the response data into dictionaries
        user_dict = r_user.json()
        true_todo_dict = r_todo_true.json()
        false_todo_dict = r_todo_false.json()

        # Display the employee's TODO list progress in the specified format
        print("Employee {} is done with tasks({}/{}):".
              format(user_dict['name'], len(true_todo_dict),
                     len(false_todo_dict) + len(true_todo_dict)))

        # Display the titles of completed tasks
        for task in true_todo_dict:
            print("\t {}".format(task['title']))

    # Handle specific exceptions that may occur during the API requests
    #  or data parsing
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection Error occurred: {conn_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request Exception occurred: {req_err}")
    except ValueError as val_err:
        print(f"ValueError occurred while parsing JSON data: {val_err}")


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        # Call the get_todo() function when the script is run as
        #  the main program
        get_todo()
