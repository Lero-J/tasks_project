from django.urls import path

from task import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_task/<int:user_id>', views.user_tasks, name='user_tasks'),
]


