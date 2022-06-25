from django.shortcuts import render, redirect
from .models import Job, Department, Worker


def workers_list(request):
    ceo = Worker.objects.get(job=1)
    managers = Worker.objects.filter(job=2)
    board = Worker.objects.filter(department=1)
    finance = Worker.objects.filter(department=2)
    attack_defence = Worker.objects.filter(department=3)
    technology = Worker.objects.filter(department=4)
    return render(request, 'workers_list.html', {'ceo': ceo,
                                                 'managers': managers,
                                                 'board': board,
                                                 'finance': finance,
                                                 'attack_defence': attack_defence,
                                                 'technology': technology
                                                 })


def redirect_home(request):
    return redirect('/')



