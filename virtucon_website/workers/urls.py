from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('jobs', views.JobView)
router.register('departments', views.DepartmentView)
router.register('workers', views.WorkerView)
urlpatterns = [
    path('api/', include(router.urls))
]