from django.shortcuts import render

from task.models import Task, User


# Create your views here.


def index(request):
    users = User.objects.all()
    ctx = { 'users': users}
    return render(request, 'task/index.html', context=ctx)

def user_tasks(request, user_id):
    user = User.objects.get(pk=user_id)
    tasks = user.task.all().filter(is_done=False)
    ctx = {'user': user, 'tasks': tasks}
    return render(request, 'task/user_tasks.html', context=ctx)





