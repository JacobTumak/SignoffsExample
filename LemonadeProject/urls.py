from django.urls import path, include
import availability_app.urls
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(availability_app.urls)),
]

