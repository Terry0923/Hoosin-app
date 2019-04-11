from .models import Student, Course, Club, Profile, Post
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
    student_list = User.objects.order_by('username')
    # student_list = User.objects.all()#values_list('username', flat=True)
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


def postDetail(request, name, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404('User not found')
    return render(request, 'profiles/postDetail.html', {'post':post})


def skillGroupDetail(request, name):
    try:
        c = Club.objects.get(name=name)
    except Club.DoesNotExist:
        raise Http404('Club not found')
    return render(request, 'profiles/skillGroupDetail.html', {'c':c})


def join(request, name, user):
    c = Club.objects.get(name=name)
    u = User.objects.get(username=user)
    c.users.add(u)
    c.save()
    return redirect('/profiles/clubs/'+name)


def leave(request, name, user):
    c = Club.objects.get(name=name)
    u = User.objects.get(username=user)
    c.users.remove(u)
    c.save()
    for pst in c.post_set.all():
        if u.profile in pst.profile.all():
            pst.profile.remove(u.profile)
    return redirect('/profiles/clubs/'+name)


def like(request, name, pk):
    p = Post.objects.get(pk=pk)
    prof = request.user.profile
    p.profile.add(prof)
    p.save()
    return redirect('/profiles/clubs/'+name+'/')


def unlike(request, name, pk):
    p = Post.objects.get(pk=pk)
    prof = request.user.profile
    p.profile.remove(prof)
    p.save()
    return redirect('/profiles/clubs/'+name+'/')


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
        return render(request, 'profiles/search_form.html')


@login_required
def profile(request):
    user = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

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
