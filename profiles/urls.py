
from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    path('students/', views.studentindex, name='student-index'),
    path('clubs/', views.clubindex, name='club-index'),
    path('students/<str:username>/', views.detail),
    url(r'^search-form/$', views.search_form, name='search-form'),
    url(r'^search/$', views.search),
]
