from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/', views.del_task, name='del_task'),
    path('toggle/<int:pk>/', views.toggle_task, name='toggle_task'),
    path('history/', views.history, name='history'),
]