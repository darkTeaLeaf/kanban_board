from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from board.models import Task, Column


def show_board(request):
    user = request.user

    if request.method == "POST":
        if request.POST.get('text') is not None:
            task = Task()
            task.text = request.POST.get('text')
            task.column = Column.objects.get(id=request.POST.get('id'))

            task.author = User.objects.get(username=user.username)
            task.save()

        if request.POST.get('title') is not None:
            column = Column()
            column.title = request.POST.get('title')

            column.author = User.objects.get(username=user.username)
            column.save()

        return redirect('/')

    elif request.method == "GET":

        columns = Column.objects.filter(author=user)
        tasks = Task.objects.filter(author=user)
        return render(request, 'board/index.html', {'columns': columns, 'tasks': tasks})
