from django.urls import path
from .views import TodoListCreateView, TodoDetailView, ToggleTodoView

urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/<int:pk>/toggle/',
         ToggleTodoView.as_view(), name='toggle_todo'),

]
