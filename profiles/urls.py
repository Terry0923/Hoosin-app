from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('students/', views.studentindex, name='student-index'),
    path('clubs/', views.clubindex, name='club-index'),
    path('students/<int:student_id>/', views.detail, name='detail')
]