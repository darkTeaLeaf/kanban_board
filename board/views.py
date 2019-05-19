from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from board.models import Task, Column


def show_board(request):

    if request.method == "POST":
        if request.POST.get('text') is not None:
            task = Task()
            task.text = request.POST.get('text')
            task.column = Column.objects.get(id=request.POST.get('id'))

            task.save()

        if request.POST.get('title') is not None:
            column = Column()
            column.title = request.POST.get('title')

            column.save()

        return redirect('/')

    elif request.method == "GET":

        columns = Column.objects.all()
        tasks = Task.objects.all()
        return render(request, 'board/index.html', {'columns': columns, 'tasks': tasks})
