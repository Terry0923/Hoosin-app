from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Student, Club, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.contrib.postgres.operations import UnaccentExtension

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
        matches_username = User.objects.filter(username__icontains=q)
        matches_first_name = User.objects.filter(first_name__icontains=q)
        matches_last_name = User.objects.filter(last_name__contains=q)
        matches_club_name = Club.objects.filter(name__icontains=q)
        # User.objects.filter(username__unaccent__icontains=q)
        return render(request, 'profiles/search_results.html',
                      {'matches_username': matches_username,
                       'matches_first_name': matches_first_name,
                       'matches_last_name': matches_last_name,
                       'matches_club_name': matches_club_name,
                       'query': q})
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
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profiles/profile.html', context)
