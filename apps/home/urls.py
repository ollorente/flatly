from django.conf.urls import include, url
from .views import *


urlpatterns = [
    url(r'^$', indexHome, name="vista_home"),
]
