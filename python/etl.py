#!/usr/bin/python3
''' script that gets employee progress '''
import requests
import sys
import json


def fetch_employee_todo_progress(employee_id):
    # Base URLs for the API
    lnk = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = lnk

    # Fetch user data
    user_response = requests.get(users_url)
    if user_response.status_code != 200:
        print(f"Failed to retrieve data for employee ID {employee_id}")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch todos data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Failed to retrieve TODO list for employee ID {employee_id}")
        return
    todos_data = todos_response.json()

    # Calculate the number of done and total tasks
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display the result

    t = f"Employee {employee_name} is done with"
    t1 = f" tasks({number_of_done_tasks}/{total_tasks}):"
    print(t + t1)
    for task in done_tasks:
        print(f"\t {task.get('title')}"



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
