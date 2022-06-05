
from django.contrib import admin
from django.urls import path
from .transform import transform_file_structure

urlpatterns = [
    path('admin/', admin.site.urls),
]

transform_file_structure()
