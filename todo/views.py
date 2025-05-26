from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from django.shortcuts import get_object_or_404
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


#! List all todos, create a new todo
class TodoListCreateView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    

#! Retrieve, update or delete one todo by id
class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


#! Toggle Todo
class ToggleTodoView(APIView):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        

        # Flip the current completed value
        todo.completed = not todo.completed
        todo.save()

        return Response({
            'message': 'Todo status toggled! 🥳',
            'completed': todo.completed
        }, status=status.HTTP_200_OK)
