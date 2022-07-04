"""
This model consists useful functions for using the api data
"""
import pathlib

import requests
import json
import numpy as np
from datetime import datetime
import os
from pathlib import Path

WORKERS_API = "http://127.0.0.1:8000/api/workers"
DEPS_API = 'http://127.0.0.1:8000/api/departments/'


def extract_api(url=WORKERS_API):
    """
    Extracting api data from a requested url.
    If an url is not mentioned the data will be extracted from the api url of all workers
    :param url: path of requested api data
    :type url: str
    :return: requested api data
    :rtype: dict or list
    """
    payload = ""
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    return data


def extract_job(worker):
    """
    Converting an api link of a worker's job to the job's name
    :param worker: the worker whose job's name is needed
    :type worker: dict
    :return: name of the worker's job
    :rtype: str
    """
    job = extract_api(worker['job'])
    return job["job_name"]


def extract_department(worker):
    """
    Converting an api link of a worker's department to the job's name
    :param worker: the worker whose department needs to be converted
    :type worker: dict
    :return: job's name
    :rtype: str
    """
    dep = extract_api(worker['department'])
    return dep['dep_name']


def get_name(worker):
    """
    Selecting how do display the worker's name.
    if the worker has a professional name, this name will be displayed.
    if he doesn't, the function will combine his first and last name to one string.
    :param worker: the worker whose name is needed
    :type worker: dict
    :return: name to display
    :rtype: str
    """
    if worker['professional_name']:
        return worker["professional_name"]
    else:
        return f'{worker["first_name"]} {worker["last_name"]}'


def get_average(workers):
    salaries = np.array(
        [worker['salary'] for worker in workers]
    )
    return np.average(salaries)


def seniority_calc(date_str):
    """
    Calculating how many years a worker has worked in the company
    :param date_str: date of the worker's first day in the company
    :type date_str: str
    :return: how many years the worker has worked in the company
    :rtype: int
    """
    date_to_check = datetime.strptime(date_str, "%Y-%m-%d")
    today = datetime.now()
    seniority = today.year - date_to_check.year
    seniority -= ((today.month, today.day) < (date_to_check.month, date_to_check.day))
    return seniority


def worker_str(worker):
    """
    Generating a long string containing the selected worker's essential details.
    :param worker: The worker needs to be represented with the string
    :type worker: dict
    :return: The string representing the worker
    :rtype: str
    """
    final_str = f'Worker: {get_name(worker)}\n'
    final_str += f'Job Description: {extract_job(worker)}\n'
    final_str += f'Department: {extract_department(worker)}\n'
    final_str += f'Hired at: {worker["hire_date"]}\n'
    final_str += f'Salary: {worker["salary"]}\n'
    return final_str


def deps_translate():
    """
    Generating a dictionary in which every key is a department api link,
    and every value is the name of the suitable department.
    this will be used for converting more than one department api link to departments names.
    :return: the dictionary mentioned above
    :rtype: dict
    """
    deps = extract_api(DEPS_API)
    deps_dict = {}
    for dep in deps:
        deps_dict.update({dep['url']: dep['dep_name']})
    return deps_dict


def worker_by_id(workers, id):
    if type(id) is int:
        for worker in workers:
            if worker['id'] == id:
                return worker
    return None


def get_img_path(worker):
    file_name = pathlib.Path(worker['profile_pic']).stem
    file_name += '.png'
    img_path = os.path.join(
        Path(__file__).resolve().parent.parent,
        'virtucon_website',
        'media',
        file_name
    )
    return img_path
