from workers.models import Job, Department, Worker
from .serializers import JobSerializer, DepartmentSerializer, WorkerSerializer
from rest_framework import viewsets, permissions


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
