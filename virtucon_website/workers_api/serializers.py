from rest_framework import serializers
from workers.models import Job, Department, Worker


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'url', 'job_name']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'url', 'dep_name']


class WorkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'url', 'first_name', 'last_name', 'professional_name', 'profile_pic', 'job', 'department',
                  'personal_motto', 'team_members', 'manager', 'salary', 'hire_date', 'email', 'phone']
