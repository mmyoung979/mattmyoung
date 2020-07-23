# Django imports
from django.urls import path

# Local imports
from . import views

# URLs
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
]
