from django.contrib import admin

from board.models import Task, Column

admin.site.register(Task)
admin.site.register(Column)
