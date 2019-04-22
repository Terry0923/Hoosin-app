from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Student, Course, Club, Profile, Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm, CommentForm
from django import forms
from django.contrib import messages
from django.contrib.auth.models import User
from itertools import chain
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import login

def home(request):
    if request.user.is_authenticated:
        return render(request,'profiles/dashboard.html')
    else:
        return render(request, 'profiles/home.html')

@login_required
def dashboard(request):
    if request.user.is_anonymous:
        return redirect('home')
    else:
        # should get profile from user, and return all of the clubs a student is in, all posts from clubs they are in
        club_list = Club.objects.filter(users=request.user)
        clubs_to_join = Club.objects.order_by('?')[:3]          # chooses 5 random clubs
        friend_list = set(request.user.profile.friends.all())
        course_list = Course.objects.filter(students=request.user)
        friends_to_make = User.objects.order_by('?')[:3]
        if len(club_list) != 0:
            c = club_list.first()
            friends_to_make = User.objects.filter(club=c).order_by('?')[:3]
        context = {
            'club_list': club_list,
            'clubs_to_join': clubs_to_join,
            'friend_list': friend_list,
            'friends_to_make': friends_to_make,
            'course_list':course_list,
        }
        return render(request, 'profiles/dashboard.html', context)


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


def addComment(request, pk, name):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CommentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = request.POST.copy()
            p = Post.objects.get(pk=pk)
            c = p.club
            comment=Comment(body=data.get('body'), date=timezone.now(), profile=request.user.profile, post=p)
            comment.save()
            return HttpResponseRedirect('/profiles/clubs/'+c.name+'/'+str(pk)+'/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    return render(request, 'profiles/comment.html', {'form': form})

def about(request):
    return render(request, 'profiles/about.html')

@login_required
def studentindex(request):
    student_list = User.objects.all()#values_list('username', flat=True)
    context = {
        'student_list': student_list
    }
    return render(request, 'profiles/studentIndex.html', context)

@login_required
def courseindex(request):
    course_list = Course.objects.order_by('title')
    context = {'course_list': course_list}
    return render(request, 'profiles/course_index.html', context)

@login_required
def clubindex(request):
    club_list = Club.objects.order_by('name')
    context = {'club_list': club_list}
    return render(request, 'profiles/club_index.html', context)

@login_required
def detail(request, username):
    try:
        uid = User.objects.get(username=username)
        cu = Profile.objects.get(user=request.user)
    except User.DoesNotExist:
        raise Http404('User not found')
    return render(request, 'profiles/detail.html', {'uid':uid, 'current_user':cu})

@login_required
def course_detail(request, title):
    try:
        course = Course.objects.get(title=title)
        cu = Profile.objects.get(user=request.user)
    except Course.DoesNotExist:
        raise Http404('Course not found')
    return render(request, 'profiles/course_detail.html', {'course':course, 'current_user':cu})

@login_required
def postDetail(request, name, pk):
    try:
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post = post)
    except Post.DoesNotExist:
        raise Http404('User not found')
    return render(request, 'profiles/postDetail.html', {'post':post, 'comments':comments})

@login_required
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

def follow(request, username, user):
    cu = Profile.objects.get(user=request.user)
    ou = User.objects.get(username=username)
    cu.friends.add(ou)
    cu.save()
    return redirect('/profiles/students/'+username)

def unfollow(request, username, user):
    cu = Profile.objects.get(user=request.user)
    ou = User.objects.get(username=username)
    cu.friends.remove(ou)
    cu.save()
    return redirect('/profiles/students/'+username)

def add_course(request, title, user):
    course = Course.objects.get(title=title)
    student = User.objects.get(username=user)
    course.students.add(student)
    course.save()
    return redirect('/profiles/courses/'+title)

def remove_course(request, title, user):
    course = Course.objects.get(title=title)
    student = User.objects.get(username=user)
    course.students.remove(student)
    course.save()
    return redirect('/profiles/courses/'+title)

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



'''
def search_form(request):
    return render(request, 'profiles/search_control.html')


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
        return render(request, 'profiles/search_control.html')
'''

@login_required
def search_control(request):
    return render(request, 'profiles/search_control.html')

@login_required
def course_search_form(request):
    return render(request, 'profiles/course_search_form.html')

@login_required
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
        return render(request, 'profiles/course_search_form.html')

@login_required
def club_search_form(request):
    return render(request, 'profiles/club_search_form.html')

@login_required
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
        return render(request, 'profiles/club_search_form.html')

@login_required
def student_search_form(request):
    return render(request, 'profiles/search_student.html')

@login_required
def student_user_search(request):
    if 'nameInput' in request.GET and request.GET['nameInput'] or 'schoolInput' in request.GET and request.GET['schoolInput'] or 'majorInput' in request.GET and request.GET['majorInput'] or 'yearInput' in request.GET and request.GET['yearInput']:
        nameInput = request.GET['nameInput']
        schoolInput = request.GET['schoolInput']
        majorInput = request.GET['majorInput']
        yearInput = request.GET['yearInput']
        u = Profile.objects.filter(user__username__icontains=nameInput,
                                    school__icontains=schoolInput,
                                    major__icontains=majorInput,
                                    year__icontains=yearInput,
                                        )
        # p = Profile.objects.filter(school__icontains=schoolInput)
        students = list(dict.fromkeys(list(chain(u))))
        return render(request, 'profiles/search_student_results.html',
                      {'matches': students, 'query':u})
    else:
        return render(request, 'profiles/search_student.html')


@login_required
def profile(request):
    user = Profile.objects.get_or_create(user=request.user)
    cu = Profile.objects.get(user=request.user)
    friends = cu.friends.all()
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
        'p_form': p_form,
        'friend_list':friends,
    }

    return render(request, 'profiles/profile.html', context)
