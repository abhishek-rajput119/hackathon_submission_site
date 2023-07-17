# Create your views here.
import os

from django.contrib.auth import login, authenticate, logout

from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
from .models import Hackathon,Profile,Registration, Submission
from .controller import HackthonUtil
from .constants import User
def user_logout(request):
    # del request.session['user_id']
    request.session.flush()
    logout(request)
    return user_login(request)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                problems = Hackathon.objects.all()
                return render(request, 'pages/home.html', {'user': user, 'problems': problems})
            else:
                return HttpResponse("Account not active")
        else:
            print("Tried login and failed")
            print("username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'pages/login.html', {})


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)

        if registered:
            problems = Hackathon.objects.all()
            return render(request, 'pages/home.html', {"user": user, 'problems': problems})

    else:
        user_form = UserForm()

    return render(request, 'pages/signup.html', {"user_form": user_form})


def home(request):
    problems = Hackathon.objects.all()
    registered_hackathon = Registration.objects.filter(user_id=request.user.id).values_list('hackathon_id')
    registered_hackathon_id_list = [entry[0] for entry in registered_hackathon]
    return render(request, 'pages/home.html', {'problems': problems, 'registered_hackathon':registered_hackathon_id_list})

def add_hackthon(request, id = None):
    if request.method == "POST":
        data,error = HackthonUtil().add_hackathon(request)
        if error == User.NOT_LOGGED_IN:
            return render(request, 'pages/login.html',{"message": "User not logged in"})
        return home(request)
    return render(request, 'pages/register_hackathon.html', {})

def register_for_hackathon(request, id=None):
    response, error = HackthonUtil().register_for_hackathon(id, request.user)   
    problems = Hackathon.objects.all()
    if error: 
        return render(request, 'pages/home.html', {'problems': problems})
    registered_hackathon = Registration.objects.filter(user_id=request.user.id).values_list('hackathon_id')
    registered_hackathon_id_list = [entry[0] for entry in registered_hackathon]
    return render(request, 'pages/home.html', {'problems': problems, 'registered_hackathon':registered_hackathon_id_list})

def make_submissions(request, hackathon_id = None):
    hackathon_object = Hackathon.objects.filter(id=hackathon_id)
    type_of_submission = hackathon_object.values()[0].get("type_of_submission")
    if request.method == "POST":
        res, error = HackthonUtil().add_submission(request.POST,request.FILES,hackathon_object[0], request.user)
        submissions = Submission.objects.filter(user_id = request.user.id, hackathon_id = hackathon_id)
        return render(request,'pages/show_submissions.html', {'problems': submissions, "hackathon_id":hackathon_id, "file_type": type_of_submission})
    return render(request,'pages/submission_page.html', {"file_type": type_of_submission})

def show_submissions(request, hackathon_id = None):
    submissions = Submission.objects.filter(user_id = request.user.id, hackathon_id = hackathon_id)
    hackathon_object = Hackathon.objects.filter(id=hackathon_id)
    type_of_submission = hackathon_object.values()[0].get("type_of_submission")
    return render(request, "pages/show_submissions.html", {'problems': submissions, "hackathon_id":hackathon_id, "file_type": type_of_submission})