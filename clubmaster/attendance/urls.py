from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.attendance_view, name = "attendance_view")
]