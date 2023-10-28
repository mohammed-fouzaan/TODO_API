# appname/urls.py
from django.urls import path
from .views import CreateUserView, UserLoginView, UserLogoutView, TasksViewSet
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='tasksviewset')

urlpatterns = [
    path('', include(router.urls)),
    path('/register/', CreateUserView.as_view(), name='user-create'),
    path('/login/', UserLoginView.as_view(), name='user-login'),
    path('/logout/', UserLogoutView.as_view(), name='user-logout'),
]
