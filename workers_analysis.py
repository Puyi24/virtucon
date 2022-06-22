import requests
import json
from statistics import mean
from datetime import datetime


def extract_api(url):
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    return data


def seniority_check(date_str):
    date_to_check = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.now()
    seniority = today.year - date_to_check.year
    seniority -= ((today.month, today.day) < (date_to_check.month, date_to_check.day))
    return seniority


def worker_to_str(worker):
    job, department = {}, {}
    final_str = f'Name: {worker["first_name"]} {worker["last_name"]}\n'
    if worker['professional_name']:
        final_str += f'Professional Name: {worker["professional_name"]}\n'
    job['job'] = extract_api(worker['job'])
    final_str += f'Job Description: {job["job"]["job_name"]}\n'
    department['department'] = extract_api(worker['department'])
    final_str += f'Department: {department["department"]["dep_name"]}\n'
    final_str += f'Salary: {worker["salary"]}\n'
    final_str += f'Hired at: {worker["hire_date"]}\n'
    final_str += '\n******************\n\n'
    return final_str


def main():
    workers_url = "http://127.0.0.1:8000/api/workers/"
    workers_data = {}
    workers_data['workers'] = extract_api(workers_url)
    average_salary = mean([worker['salary'] for worker in workers_data['workers']])
    with open('discriminated_workers.txt', 'w') as result_file:
        for worker in workers_data['workers']:
            if worker['salary'] < average_salary and seniority_check(worker['hire_date']) >= 1:
                result_file.write(worker_to_str(worker))


if __name__ == "__main__":
    main()
