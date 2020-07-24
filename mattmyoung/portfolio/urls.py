# Django imports
from django.urls import path, include

# Project imports
from . import views
from ..zerocater import urls as zerocater
from ..egan_jones import urls as egan_jones

# URLs
urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('pts/', views.pts, name='pts'),
    path('plotly/', views.plotly, name='plotly'),
    path('zerocater/', include(zerocater)),
    path('egan-jones/', include(egan_jones)),
]
