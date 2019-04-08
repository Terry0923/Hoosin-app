
from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    path('students/', views.studentindex, name='student-index'),
    path('clubs/', views.clubindex, name='club-index'),
    path('students/<str:username>/', views.detail, name='student-detail'),
    path('clubs/<str:name>/', views.skillGroupDetail),
    path('clubs/<str:name>/<str:user>/join', views.join),
    path('clubs/<str:name>/<str:user>/leave', views.leave),
    path('clubs/<str:name>/add-post/', views.addPost, name='add-post'),
    url(r'^search-form/$', views.search_form, name='search-form'),
    url(r'^search/$', views.search, name='search-results'),
]
