# Django imports
from django.urls import path

# Project imports
from . import views


# URLS
urlpatterns = [
    path('', views.index, name='ej'),
    path('cash-flows', views.cash_flows, name='ej_cash_flows'),
    path('cash-flows/<ticker>', views.detail_view, name='ej_detail_view'),
    path('list-view/', views.list_view, name='ej_list_view'),
]
