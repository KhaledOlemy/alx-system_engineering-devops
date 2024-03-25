#!/usr/bin/python3
"""
Get all employees task progress and export to .json
USAGE: 3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests
import sys

if __name__ == "__main__":
    main_url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(main_url).json()
    out_dict = {}
    for user in users:
        url = f"{main_url}{user.get('id')}/todos"
        emp_req = requests.get(url).json()
        tasks = []
        for task in emp_req:
            tc = task['completed']
            tt = task['title']
            en = user.get("username")
            task_item = {"task": tt, "completed": tc, "username": en}
            tasks.append(task_item)
        if tasks:
            tid = task['userId']
            out_dict[str(tid)] = tasks
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(out_dict, jsonfile)
