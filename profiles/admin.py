from django.contrib import admin
from .models import Student, Course, Club, Profile, Post

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Club)
admin.site.register(Profile)
admin.site.register(Post)
