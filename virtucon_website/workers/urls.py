from django.urls import path
from . import views

app_name = 'workers_app'
urlpatterns = [
    path('', views.redirect_home, name='go_home')
]
