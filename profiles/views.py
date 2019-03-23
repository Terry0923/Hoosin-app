from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Student, Club
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django import forms
from django.contrib import messages

def studentindex(request):
    student_list = Student.objects.order_by('name')
    context = {'student_list': student_list}
    return render(request, 'profiles/studentIndex.html', context)


def clubindex(request):
    club_list = Club.objects.order_by('name')
    context = {'club_list': club_list}
    return render(request, 'profiles/clubIndex.html', context)


def detail(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'profiles/detail.html', {'student': student})


@login_required
def profile(request):
    return render(request,'profiles/profile.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if "@virginia.edu" in email:
                messages.success(request, f'Your account has been created! You are now able to log in')
                return redirect('login')
            else:
                return render(request, 'profiles/error.html')
    else:
        form = UserRegisterForm()
    return render(request, 'profiles/register.html', {'form': form})
