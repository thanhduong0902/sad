# urls.py

from django.urls import path
from .views import home

urlpatterns = [
    path('books/', home, name='home'),
]
