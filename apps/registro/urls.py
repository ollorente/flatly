from django.conf.urls import url

from .views import *


urlpatterns = [
	url(r'^$', indexRegister, name='vista_registro'),
]
