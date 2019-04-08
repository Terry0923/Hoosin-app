from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Student, Club, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from itertools import chain
from django.db.models import Q


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


def club_search_form(request):
    return render(request, 'profiles/club_search_form.html')

def student_search_form(request):
    return render(request, 'profiles/search_student.html')


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

def student_search(request):
    if 'schoolInput' in request.GET and request.GET['schoolInput']:
        schoolInput = request.GET['schoolInput']
        nameInput = request.GET['nameInput']
        school_name = Profile.objects.filter(school__icontains=schoolInput).select_related('user')
        # user_name = school_name.
        students = list(dict.fromkeys(list(chain(school_name))))
        return render(request, 'profiles/search_student_results.html',
                      {'matches': students, 'query': schoolInput})
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
