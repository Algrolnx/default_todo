from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'tasks'

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')
router.register(r'history', views.TaskHistoryViewSet, basename='history')

urlpatterns = [
    path('', include(router.urls)),
]
