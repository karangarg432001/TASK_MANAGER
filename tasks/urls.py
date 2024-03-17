from django.urls import path, include
from .views import LoginView, RegisterView, TaskListCreate, TaskRetrieveUpdateDestroy
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API", 
        default_version='v1',
        description="API documentation for the Task Manager API",
        contact=openapi.Contact(email="karangarg432001@gmail.com")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
    )

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update-destroy'),
    path('swag_docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
