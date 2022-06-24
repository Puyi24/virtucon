from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('jobs', views.JobView)
router.register('departments', views.DepartmentView)
router.register('workers', views.WorkerView)
urlpatterns = [
    path('', include(router.urls))
]
