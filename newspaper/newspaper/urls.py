
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('feednews/', include('feednews.urls')),
    path('admin/', admin.site.urls),
]
