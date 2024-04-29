from django.urls import path

from apps.todos.views import todo, todo_add, todo_create, DeleteViewPage, UpdateViewPage, DetailViewPage

urlpatterns = [
    path('', todo, name='todo-page'),
    path('todo_add/', todo_add, name='todo_add-page'),
    path('todo_create/', todo_create, name='todo_create-page'),
    path('delete/<int:pk>', DeleteViewPage.as_view(), name='delete-page'),
    path('update/<int:pk>', UpdateViewPage.as_view(), name='update-page'),
    path('detail/<int:pk>', DetailViewPage.as_view(), name='detail-page'),
]