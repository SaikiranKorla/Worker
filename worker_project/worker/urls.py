# worker/urls.py

from django.urls import path
from .views import home, register_worker, update_worker

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_worker, name='register_worker'),
    path('update/<int:worker_id>/', update_worker, name='update_worker'),
    # Add other URL patterns if needed
]
