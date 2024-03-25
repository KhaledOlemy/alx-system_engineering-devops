#!/usr/bin/python3
"""
Get employee tasks details with employeeID
USAGE: 0-gather_data_from_an_API.py employeeID
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = eval(sys.argv[1])
    main_url = "https://jsonplaceholder.typicode.com/users/"
    emp_req = requests.get(f"{main_url}{employee_id}/todos").json()
    e_name = requests.get(f"{main_url}{employee_id}/").json().get('name')
    n_tasks = len(emp_req)
    tasks_done = [i for i in emp_req if i.get('completed')]
    nd_tasks = len(tasks_done)
    e_status = f"Employee {e_name} is done with tasks({nd_tasks}/{n_tasks}):"
    print(e_status)
    for task in tasks_done:
        print(f"\t {task.get('title')}")
