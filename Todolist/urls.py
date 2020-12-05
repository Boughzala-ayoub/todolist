
from django.contrib import admin
from django.urls import path
from todo.views import todoView, addTodo, deleteTodo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoView, name='todo'),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
]
