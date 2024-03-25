#!/usr/bin/python3
import requests
import sys


employee_id = eval(sys.argv[1])
main_url = "https://jsonplaceholder.typicode.com/users/"
emp_req = requests.get(f"{main_url}{employee_id}/todos").json()
e_name = requests.get(f"{main_url}{employee_id}/").json().get('name')
n_tasks = len(emp_req)
tasks_done = [i for i in emp_req if i.get('completed')]
nd_tasks = len(tasks_done)
e_statement = f"Employee {e_name} is done with tasks({nd_tasks}/{n_tasks}):"
print(e_statement)
for task in tasks_done:
    print(f"\t {task.get('title')}")
