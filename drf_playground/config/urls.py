from django.contrib import admin
from django.urls import path, include
import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drf_app.urls'))
]
