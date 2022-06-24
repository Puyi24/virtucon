from django.shortcuts import render, redirect
from .models import Job, Department, Worker


def workers_list(request):
    ceo = Worker.objects.get(job=1)
    managers = Worker.objects.filter(job=2)
    workers = Worker.objects.exclude(job=1).exclude(job=2)
    return render(request, 'workers_list.html', {'ceo': ceo,
                                                 'managers': managers,
                                                 'workers': workers})


def redirect_home(request):
    return redirect('/')



