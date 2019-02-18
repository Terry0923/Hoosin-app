from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student, Club


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
