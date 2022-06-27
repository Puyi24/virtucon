from django.shortcuts import render, redirect, HttpResponse
from .models import Job, Department, Worker
import json
import pymongo
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
JSON_PATH = os.path.join(BASE_DIR, 'json_files')


def redirect_home(request):
    return redirect('/')


def restore_db():
    mon_client = pymongo.MongoClient('mongodb://localhost:27017/')
    mon_db = mon_client['virtucon_db']
    with open(os.path.join(JSON_PATH, 'jobs.json'), 'r') as jobs_file, \
            open(os.path.join(JSON_PATH, 'departments.json'), 'r') as deps_file, \
            open(os.path.join(JSON_PATH, 'workers.json'), 'r') as workers_file, \
            open(os.path.join(JSON_PATH, 'worker_team_members.json'), 'r') as teams_file:
        data = json.load(jobs_file)
        mon_db['workers_job'].insert_many(data['jobs'])
        data = json.load(deps_file)
        mon_db['workers_department'].insert_many(data['departments'])
        data = json.load(workers_file)
        mon_db['workers_worker'].insert_many(data['workers'])
        data = json.load(teams_file)
        mon_db['workers_worker_team_members'].insert_many(data['worker_team_members'])


def workers_list(request):
    if Worker.objects.count() == 0:
        restore_db()
    ceo = Worker.objects.get(job=1)
    managers = Worker.objects.filter(job=2)
    workers = Worker.objects.exclude(job=1).exclude(job=2).order_by('department')
    board = Worker.objects.filter(department=1).exclude(id=1)
    finance = Worker.objects.filter(department=2).exclude(job=2)
    attack_defence = Worker.objects.filter(department=3).exclude(job=2)
    technology = Worker.objects.filter(department=4).exclude(job=2)
    return render(request, 'workers_list.html', {'ceo': ceo,
                                                 'managers': managers,
                                                 'board': board,
                                                 'workers': workers,
                                                 'finance': finance,
                                                 'attack_defence': attack_defence,
                                                 'technology': technology
                                                 })

