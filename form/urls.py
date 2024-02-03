#urls.py
from django.contrib import admin
from django.urls import include, path
from formapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('formapp.urls')),
]
