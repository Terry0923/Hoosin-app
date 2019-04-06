
from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    path('students/', views.studentindex, name='student-index'),
    path('clubs/', views.clubindex, name='club-index'),
    path('students/<str:username>/', views.detail),
    path('clubs/<str:name>/', views.club_detail),
    url(r'^search-control/$', views.search_control, name='search-control'),
    url(r'^club-search-form/$', views.club_search_form, name='club-search-form'),
    url(r'^club-search/$', views.club_search, name='club-search'),
]
