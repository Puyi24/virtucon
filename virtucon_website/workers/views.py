from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Job, Department, Worker
from .serializers import JobSerializer, DepartmentSerializer, WorkerSerializer

def workers_list(request):
    workers = Worker.objects.all().order_by('id')
    return render(request, 'workers_list.html', {'workers': workers})

class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class WorkerView(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)