
from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    path('students/', views.studentindex, name='student-index'),
    path('courses/', views.courseindex, name='course-index'),
    path('clubs/', views.clubindex, name='club-index'),
    path('students/<str:username>/', views.detail),
    path('courses/<str:title>/', views.course_detail),
    path('clubs/<str:name>/', views.club_detail),
    url(r'^search-control/$', views.search_control, name='search-control'),
    url(r'^course-search-form/$', views.course_search_form, name='course-search-form'),
    url(r'^course-search/$', views.course_search, name='course-search'),
    url(r'^club-search-form/$', views.club_search_form, name='club-search-form'),
    url(r'^club-search/$', views.club_search, name='club-search'),
]
