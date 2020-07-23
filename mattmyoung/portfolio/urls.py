# Django imports
from django.urls import path

# Project imports
from . import views

# URLs
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('pts/', views.pts, name='pts'),
    path('plotly/', views.plotly, name='plotly'),
]
