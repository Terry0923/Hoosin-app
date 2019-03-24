from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    path('students/', views.studentindex, name='student-index'),
    path('clubs/', views.clubindex, name='club-index'),
    #path('students/<int:student_id>/', views.detail, name='detail'),
    #path('search-form/', views.search_form),
    #path('search/', views.search),
    path('students/<str:username>/', views.detail),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
]
