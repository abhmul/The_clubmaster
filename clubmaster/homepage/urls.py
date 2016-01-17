from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/$', views.user_registration, name = 'home'),
	url(r'^dashboard/$', views.dashboard, name = 'dashboard_home')
]