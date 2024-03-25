#!/usr/bin/python3
"""
Get employee tasks details with employeeID and export to .csv
USAGE: 1-export_to_CSV.py employeeID
"""
import requests
import sys
import time

if __name__ == "__main__":
    employee_id = eval(sys.argv[1])
    main_url = "https://jsonplaceholder.typicode.com/users/"
    emp_req = requests.get(f"{main_url}{employee_id}/todos").json()
    e_name = requests.get(f"{main_url}{employee_id}/").json().get('name')
    out_csv = ""
    # for task in emp_req:
    #     tid = task['userId']
    #     cp = task['completed']
    #     tt = task['title']
    #     out_csv += f""""{tid}","{e_name}","{cp}","{tt}" """.strip()
    #     out_csv += "\n"
    #     l = line = '"' + str(task['userId']) + '","' + e_name + '","' + str(task['completed']) + '","' + task['title'] + '"'
    # with open(f"{employee_id}.csv", "w") as csvfile:
    #     csvfile.write(out_csv)
    with open(f"{employee_id}.csv", "a") as csvfile:
        for task in emp_req:
            tid = task['userId']
            cp = task['completed']
            tt = task['title']
            l = '"' + str(task['userId']) + '","' + e_name + '","' + str(task['completed']) + '","' + task['title'] + '"\n'
            csvfile.write(l)
