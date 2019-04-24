from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.show_board, name='board'),
]