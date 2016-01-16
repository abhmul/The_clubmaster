from django.shortcuts import render, redirect
from authentication.forms import UserRegistration, OrganizationRegistration
from django.contrib.auth import authenticate, login
from django.cotnrib.auth.models import User



def index(request):
	 """
	 A view that displays the homepage of the website
	 """
	context = {}
	return render(request, 'homepage/index.html', context)

def user_registration(request):
	"""
	A view for allowing users to register themselves or as an organization
	"""
	title = 'Registration'
	context = {}
	form = UserRegistration(request.POST or None)
	if form.isValid():
		"""
		tests if an email has already been used
		"""
		if User.objects.filter(email = form.cleaned_data['email']).exists(): #tests for previously used emails
            error = "Email already in use"
            context = {
                'title': title,
                'error': error,
                'form': form
                }

            return render(request, 'homepage/homepage_template.html', context)
		
		if forms.cleaned_data['password'] != form.cleaned_data['confirm_password']: # tests for non matching passowrds 
			error = "Passwords don't match"
			context = {
				'title': title,
				'error': error,
				'form': form
			}

			return render(request, 'homepage/homepage_template.html', context)

		if len(forms.cleaned_data['password']) < 8: # tests for too short passwords (less than 8 characters)
			error = "Password is too short, must be at least 8 characters"
			context = {
				'title':title,
				'error':error,
				'form':form
			}

			return render(request, 'homepage/homepage_template.html', context)

		else:
			try:
				user = User.objects.create_user( # create a new user object
									email = form.cleaned_data['email'],
									first_name = form.cleaned_data['first_name'],
									last_name = form.cleaned_data['last_name'],
									username = form.cleaned_data['email'], # users use their emails as usernames by default
									password = form.cleaned_data['password']
									)
				title = 'Register an Organization'
				form = OrganizationRegistration(request.POST or None)
				context = {
					'form': form
				}

				return redirect('homepage_template', context)

			except IntegrityError: # prevents a user from registering a previously used username
				error = 'Username already taken'
				context = {
					'title':title,
					'form':form,
					'error':error
				}
				return render(request, 'homepage/homepage_template.html', context)

			auth_user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            login(request, auth_user)
			return render(request, 'homepage/homepage_template.html', context)

	return render(request, 'homepage/homepage_template.html')




											



