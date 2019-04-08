from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Student, Course, Club, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from itertools import chain


def home(request):
    return render(request, 'profiles/home.html')


def about(request):
    return render(request, 'profiles/about.html')


def studentindex(request):
    #student_list = Student.objects.order_by('username')
    student_list = User.objects.all()#values_list('username', flat=True)
    context = {
        'student_list': student_list
    }
    return render(request, 'profiles/studentIndex.html', context)


def courseindex(request):
    course_list = Course.objects.order_by('title')
    context = {'course_list': course_list}
    return render(request, 'profiles/courseIndex.html', context)


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


def course_detail(request, title):
    try:
        uid = Course.objects.get(title=title)
    except Course.DoesNotExist:
        raise Http404('Course not found')
    return render(request, 'profiles/course_detail.html', {'uid':uid})


def club_detail(request, name):
    try:
        uid = Club.objects.get(name=name)
    except Club.DoesNotExist:
        raise Http404('Skill group not found')
    return render(request, 'profiles/club_detail.html', {'uid':uid})


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


def search_control(request):
    return render(request, 'profiles/search_control.html')


def course_search_form(request):
    return render(request, 'profiles/course_search_form.html')


def course_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        # users = User.objects.filter(username__icontains=q)
        course_title = Course.objects.filter(title__icontains=q)
        course_desc = Course.objects.filter(description__icontains=q)
        courses = list(dict.fromkeys(list(chain(course_title, course_desc))))
        return render(request, 'profiles/search_results.html',
                      {'matches': courses, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def club_search_form(request):
    return render(request, 'profiles/club_search_form.html')


def club_search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        # users = User.objects.filter(username__icontains=q)
        club_name = Club.objects.filter(name__icontains=q)
        club_desc = Club.objects.filter(description__icontains=q)
        clubs = list(dict.fromkeys(list(chain(club_name, club_desc))))
        return render(request, 'profiles/search_results.html',
                      {'matches': clubs, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


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
