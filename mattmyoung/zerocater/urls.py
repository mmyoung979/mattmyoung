# Django imports
from django.urls import path

# Project imports
from . import views

# URLs
urlpatterns = [
    path('', views.zerocater, name='zerocater'),
]
