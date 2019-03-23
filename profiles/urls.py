from django.urls import path

from . import views
from hoosin import pipeline

app_name = 'profiles'
urlpatterns = [
    path('students/', views.studentindex, name='student-index'),
    path('clubs/', views.clubindex, name='club-index'),
    path('<int:student_id>/', views.detail, name='detail'),
    path('error/', views.register, name='error')
]
