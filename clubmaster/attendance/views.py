from django.shortcuts import render
from .models import Member
from django.contrib.auth.models import User
from organizations.models import Organization

from .forms import MemberCreationForm

# Create your views here.

def attendance_view(request):

	current_user = User.objects.get(id = request.session['_auth_user_id'])
	organization = Organization.objects.get(identifier = 'chang gang')
	member_list = Member.objects.filter(organization = organization)
	member_attrs = []
	for member in member_list:
		atrr = member.to_list
		member_attrs.append(attr)
	form = MemberCreationForm(request.POST or None)
	context = {'form':form}
	if form.is_valid():
		Member(first_name = form.cleaned_data['first_name']
	    last_name = form.cleaned_data['last_name']
	    email = form.cleaned_data['phone_number']
	    phone_number = form.cleaned_data['phone_number']
	    college = form.cleaned_data['college']
	    grad_year = form.cleaned_data['grad_year']).save()
		
	return render(request, 'attendance/attendance.html', context)