import json
import pymongo

mon_client = pymongo.MongoClient('mongodb://localhost:27017/')
mon_db = mon_client['virtucon_db']
with open('jobs.json', 'r') as jobs_file:
    data = json.load(jobs_file)
    mon_db['workers_job'].insert_many(data['jobs'])
with open('departments.json', 'r') as deps_file:
    data = json.load(deps_file)
    mon_db['workers_department'].insert_many(data['departments'])
with open('workers.json', 'r') as workers_file:
    data = json.load(workers_file)
    mon_db['workers_worker'].insert_many(data['workers'])
with open('worker_team_members.json', 'r') as teams_file:
    data = json.load(teams_file)
    mon_db['workers_worker_team_members'].insert_many(data['worker_team_members'])
