from django.contrib import admin
from django.urls import path, include

from user_service import urls as users_urls
from .swagger import swagger_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_urls))
] + swagger_urls
