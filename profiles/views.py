from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Student, Club, Profile, Post
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from itertools import chain
from django.utils import timezone
from django.urls import reverse

def home(request):
    return render(request, 'profiles/home.html')


def addPost(request, name):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = request.POST.copy()
            c = Club.objects.get(name=name)
            if name == c.name:
                post = Post(headline = data.get('headline'), date=timezone.now(), type = data.get('type'), body = data.get('body'), club = c)
                post.save()
                # redirect to a new URL:
                return HttpResponseRedirect('/profiles/clubs/'+c.name+'/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    return render(request, 'profiles/post.html', {'form': form})

def about(request):
    return render(request, 'profiles/about.html')


def studentindex(request):
    #student_list = Student.objects.order_by('username')
    student_list = User.objects.all()#values_list('username', flat=True)
    context = {
        'student_list': student_list
    }
    return render(request, 'profiles/studentIndex.html', context)


def clubindex(request):
    club_list = Club.objects.order_by('name')
    context = {'club_list': club_list}
    return render(request, 'profiles/clubIndex.html', context)


def detail(request, username):
    try:
        uid = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404('User not found')
    return render(request, 'profiles/detail.html', {'uid':uid})


def skillGroupDetail(request, name):
    try:
        c = Club.objects.get(name=name)
    except Club.DoesNotExist:
        raise Http404('Club not found')
    return render(request, 'profiles/skillGroupDetail.html', {'c':c})


def join(request, c):
    return render(request, 'profiles/skillGroupDetail.html', {'c':c})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})

def search_form(request):
    return render(request, 'profiles/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        users = User.objects.filter(username__icontains=q)
        club_name = Club.objects.filter(name__icontains=q)
        club_desc = Club.objects.filter(description__icontains=q)
        clubs = list(dict.fromkeys(list(chain(club_name, club_desc))))
        # matches = chain(users, clubs)
        return render(request, 'profiles/search_results.html',
                      {'user_matches': users, 'club_matches': clubs, 'query': q})
    else:
        return render(request, 'profiles/search_form.html')

@login_required
def profile(request):
    user = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        # p_form = ProfileUpdateForm(request.POST,
        #                           request.FILES,
        #                           instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profiles/profile.html', context)
