from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


# List all todos, create a new todo
class TodoListCreateView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Retrieve, update or delete one todo by id


class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
