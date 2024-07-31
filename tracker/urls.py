from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.create_project, name='create_project'),
    path('project/<int:project_pk>/issue/new/', views.create_issue, name='create_issue'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
]