from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/$', views.index, name = 'home'),
	url(r'^', views.index, name='index')
]