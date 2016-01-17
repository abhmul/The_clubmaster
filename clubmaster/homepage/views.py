from django.shortcuts import render, redirect
from authentication.forms import UserRegistration
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from organizations.models import Organization




# def index(request):
#     """
#     A view that displays the homepage of the website
#     """
#     context = {}
#     return render(request, 'homepage/registration_template.html', context)


def user_registration(request):
    """
    A view for allowing users to register themselves or as an organization
    """
    title = 'Registration'
    

    form = UserRegistration(request.POST or None)

    context = {
        'form':form,
        'title':title,
    }
    # print form.is_valid()
    if form.is_valid():
        """
        tests if an email has already been used
        """
        # print form.is_valid()
        if User.objects.filter(email=form.cleaned_data['email']).exists():  # tests for previously used emails
            error = "Email already in use"
            context = {
                'title': title,
                'error': error,
                'form': form
            }

        if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:  # tests for non matching passowrds
            error = "Passwords don't match"
            context = {
                'title': title,
                'error': error,
                'form': form
            }

        if len(form.cleaned_data['password']) < 8:  # tests for too short passwords (less than 8 characters)
            error = "Password is too short, must be at least 8 characters"
            context = {
                'title': title,
                'error': error,
                'form': form
            }

        else:
            try:
                user = User.objects.create_user(  # create a new user object
                                                  email=form.cleaned_data['email'],
                                                  first_name=form.cleaned_data['first_name'],
                                                  last_name=form.cleaned_data['last_name'],
                                                  username=form.cleaned_data['email'],
                                                  # users use their emails as usernames by default
                                                  password=form.cleaned_data['password']
                                                  )
                print "user created"
                Organization(identifier=form.cleaned_data['org_name'], name =form.cleaned_data['org_name'], website = form.cleaned_data['website'], contact = form.cleaned_data['contact'], description = form.cleaned_data['description']).save()
                
            except IntegrityError:  # prevents a user from registering a previously used username
                error = 'Username already taken'
                context = {
                    'title': title,
                    'form': form,
                    'error': error
                }
                return render(request, 'homepage/registration_template.html', context)

            auth_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, auth_user)
            print "hey1"
            return render(request, 'homepage/registration_template.html', context)
        print "hey2"
        return render(request, 'homepage/registration_template.html', context)
    print "hey3"
    return render(request, 'homepage/registration_template.html', context)

def dashboard_test(request):
    context = {}
    return render(request, 'homepage/dashboard.html', context)


