from django.urls import path

from .services import add_item, delete_item
from .views import TaskListView



urlpatterns = [
    path('', TaskListView.as_view()),
    path('add/', add_item),
    path('delete/<int:object>', delete_item),


]