from django.urls import re_path as url
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index')
]