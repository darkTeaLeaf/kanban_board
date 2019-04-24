from django import template

register = template.Library()


@register.filter
def get_column_tasks(request, column):
    column_tasks = request.filter(column=column)
    return column_tasks
