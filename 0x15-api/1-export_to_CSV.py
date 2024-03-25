#!/usr/bin/python3
"""
Get employee tasks details with employeeID and export to .csv
USAGE: 1-export_to_CSV.py employeeID
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = eval(sys.argv[1])
    main_url = "https://jsonplaceholder.typicode.com/users/"
    emp_req = requests.get(f"{main_url}{employee_id}/todos").json()
    e_name = requests.get(f"{main_url}{employee_id}/").json().get('username')
    out_csv = ""
    with open(f"{employee_id}.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in emp_req:
            tid = task['userId']
            tc = task['completed']
            tt = task['title']
            csv_writer.writerow([tid, e_name, tc, tt])
