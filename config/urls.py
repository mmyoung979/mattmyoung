# Django imports
from django.contrib import admin
from django.urls import path, include

# Project imports
from mattmyoung.frontend import urls as frontend
from mattmyoung.portfolio import urls as portfolio

# URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(frontend)),
    path('portfolio/', include(portfolio)),
]
