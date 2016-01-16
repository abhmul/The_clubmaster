from django.shortcuts import render

# Create your views here.


def login(request):

	# sets up the view for the login page where users can login/register

	context = {}
	return render(request, 'login.html', context)