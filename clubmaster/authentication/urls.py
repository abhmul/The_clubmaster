from django.conf.urls import url
from . import views

urls = [
	url(r'^login/$', views.login, name="login")
]