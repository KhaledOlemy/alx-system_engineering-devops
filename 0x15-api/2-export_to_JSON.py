#!/usr/bin/python3
"""
Get employee tasks details with employeeID and export to .json
USAGE: 1-export_to_JSON.py employeeID
"""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = eval(sys.argv[1])
    main_url = "https://jsonplaceholder.typicode.com/users/"
    emp_req = requests.get(f"{main_url}{employee_id}/todos").json()
    e_name = requests.get(f"{main_url}{employee_id}/").json().get('username')
    tasks = []
    for task in emp_req:
        tc = task['completed']
        tt = task['title']
        task_item = {"task": tt, "completed": tc, "username": e_name}
        tasks.append(task_item)
        if tasks:
            tid = task['userId']
            out_dict = {tid: tasks}
    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(out_dict, jsonfile)
