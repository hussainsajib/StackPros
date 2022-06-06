
from django.contrib import admin
from django.urls import path, include
from .transform import transform_file_structure

urlpatterns = [
    path('admin/', admin.site.urls),
    path('path/', include('filesystem.urls')),
]

transform_file_structure()
