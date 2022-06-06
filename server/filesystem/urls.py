from django.urls import path

from . import views

urlpatterns = [
    path('', views.file_structure, name='file_structure'),
]
