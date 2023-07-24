#!/usr/bin/python3
"""
Returns information about his/her TODO list progress for a
given employee ID using a REST API and exports the data to a CSV file.
"""
import csv
import requests
from sys import argv


def get_todo_csv():
    """Fetches and exports employee's TODO list progress to a CSV file"""

    # Make a GET request to fetch the user data using the given employee ID
    r_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                          .format(argv[1]))

    # Make a GET request to fetch the TODO list data associated with
    #  the same user ID
    r_todo = requests.get('https://jsonplaceholder.typicode.com/todos?'
                          'userId={}'.format(argv[1]))

    try:
        # Check if both requests were successful (status code 200)
        r_user.raise_for_status()
        r_todo.raise_for_status()

        # Parse the JSON response into dictionaries
        user_dict = r_user.json()
        task_dict = r_todo.json()

        # Open a new CSV file with the name "<employee_id>.csv" in write mode
        with open("{}.csv".format(argv[1]), "w") as csvfile:
            # Create a CSV writer object using ',' as the delimiter and
            #  quoting all fields
            f = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

            # Write each task's data to the CSV file as a row
            for task in task_dict:
                f.writerow([user_dict["id"], user_dict["username"],
                            task["completed"], task["title"]])
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    except ValueError as e:
        print(f"Error parsing JSON data: {e}")


if __name__ == "__main__":
    # Execute the get_todo_csv() function when the script is run
    get_todo_csv()
