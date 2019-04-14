
from django.urls import path, include
from django.conf.urls import url

from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.studentindex, name='student-index'),
    path('courses/', views.courseindex, name='course-index'),
    path('clubs/', views.clubindex, name='club-index'),
    path('students/<str:username>/', views.detail, name='student-detail'),
    path('students/<str:username>/<str:user>/follow/',views.follow, name='follow'),
        path('students/<str:username>/<str:user>/unfollow/',views.unfollow, name='unfollow'),
    path('courses/<str:title>/', views.course_detail),
    path('clubs/<str:name>/', views.skillGroupDetail),
    path('clubs/<str:name>/<str:user>/join', views.join),
    path('clubs/<str:name>/<str:user>/leave', views.leave),
    path('clubs/<str:name>/<int:pk>/', views.postDetail),
    path('clubs/<str:name>/<int:pk>/like', views.like),
    path('clubs/<str:name>/<int:pk>/unlike', views.unlike),
    path('clubs/<str:name>/add-post/', views.addPost, name='add-post'),
    path('clubs/<str:name>/<int:pk>/add-comment/', views.addComment, name='add-comment'),
    url(r'^search-control/$', views.search_control, name='search-control'),
    url(r'^course-search-form/$', views.course_search_form, name='course-search-form'),
    url(r'^course-search/$', views.course_search, name='course-search'),
    url(r'^club-search-form/$', views.club_search_form, name='club-search-form'),
    url(r'^club-search/$', views.club_search, name='club-search'),
    # url(r'^search-form/$', views.search_form, name='search-form'),
    # url(r'^search/$', views.search, name='search-results'),
]
