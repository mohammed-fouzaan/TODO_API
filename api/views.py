from asyncio import tasks
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserLoginSerializer, UserSerializer, TasksSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.views import obtain_auth_token
from api.models import Tasks
from .permissions import IsOwner
import time

class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        print(request.data)
        data = request.data
        reg_serializer = UserSerializer(data=data)
        if reg_serializer.is_valid():
            password = reg_serializer.validated_data.get('password')
            reg_serializer.validated_data['password']=make_password(password)
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user:
                    login(request, user)
                    print(request,user)
                    sessionid = request.session.session_key
                    csrftoken = request.META.get('CSRF_COOKIE')
                    return Response({'message': 'Login successful', 'sessionid':sessionid,'csrftoken':csrftoken}, status=status.HTTP_200_OK)
                else:
                    return Response({'message': 'User is not a staff member'}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    def post(self, request, format=None):
        logout(request)
        print("loggedout")
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsOwner]
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)