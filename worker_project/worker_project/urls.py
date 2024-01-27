# worker_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('worker.urls')),  # Include the worker app's URLs
    # Add other URL patterns if needed
]
