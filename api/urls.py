from django.urls import path
from . import views

urlpatterns = [
    path('', views.getTodos),
    path('add-todo/', views.addTodo),
    path('delete-todo/<str:pk>/', views.deleteTodo),
    path('update-todo/<str:pk>/', views.updateTodo)
]
