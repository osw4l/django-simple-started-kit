from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url(r'^app/', include('apps.api.app.urls')),
]
