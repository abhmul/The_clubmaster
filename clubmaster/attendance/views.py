from django.shortcuts import render
from .models import Member
from django.contrib.auth.models import User
from organizations.models import Organization

# Create your views here.

def attendance_view(request):

	current_user = User.objects.get(id = request.session['_auth_user_id'])
	organization = Organization.objects.get(identifier = 'chang gang')
	member_list = Member.objects.filter(organization = organization)
	member_attrs = []
	for member in member_list:
		atrr = member.to_list
		member_attrs.append(attr)
	context = {}
	return render(request, 'attendance/attendance.html', context)