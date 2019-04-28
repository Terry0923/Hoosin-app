#test cases for forms.py

from django.test import TestCase
from django.test import Client
from .forms import *
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Register_Form_Test(TestCase):

    def test_RegisterForm_valid(self):
        form = UserRegisterForm(data={
        'username':"Terry",
        'email':"jt2fx@virginia.edu",
        'password1':"testing321",
        'password2':"testing321",
        })
        self.assertTrue(form.is_valid())
        ###Terminal says otherwise

    def test_RegisterForm_invalid(self):
        form = UserRegisterForm(data={
        'email': "terry@virginia.edu"
        })
        self.assertFalse(form.is_valid())
        ###Terminal syas otherwise

    def test_mismatch_password_invalid(self):
        form = UserRegisterForm(data={
        'username':"Terry",
        'email':"jt2fx@virginia.edu",
        'password1':"testing123",
        'password2':"testing321",
        })
        self.assertFalse(form.is_valid())

    def test_virginia_email_form_invalid(self):
        form = UserRegisterForm(data={
        'username':"Terry",
        'email':"jt2fx@yahoo.com.tw",
        'password1':"testing321",
        'password2':"testing321",
        })
        self.assertFalse(form.is_valid())


class User_Update_Form_Test(TestCase):

    def test_UserUpdateForm_valid(self):
        form = UserUpdateForm(data={'username':'user','email':"user@virginia.edu"})
        self.assertTrue(form.is_valid())

    def test_UserUpdateForm_invalid(self):
        form = UserUpdateForm(data={'email':"user@virginia.edu"})
        self.assertFalse(form.is_valid())

class Profile_Update_Form_Test(TestCase):

    def test_ProfleUpdateForm_valid(self):
        form = ProfileUpdateForm(data={ 'image':'default.jpg',
                                        'status':'looking for a study buddy',
                                        'year':'first',
                                        'major':'Computer Science',
                                        'school':'School of Nursing',
                                        'bio':'Im cool',
                                        })
        self.assertTrue(form.is_valid())

        #test if missing fields
    def test_PrrofileUpdateForm_invalid(self):
        form = ProfileUpdateForm(data={ 'status':'looking for a study buddy',
                                        'year':'first',
                                        'major':'Computer Science',
                                        'school':'School of Nursing',
                                        })
        self.assertFalse(form.is_valid())

class Post_Form_Test(TestCase):

    def test_PostForm_valid(self):
        form = PostForm(data={'headline':"I love Kobe",
                                'body':"He a great player",
                                'type':'announcement'})
        self.assertTrue(form.is_valid())

    def test_PostForm_invalid(self):
        form = PostForm(data={'headline':"I love Kobe",
                                'type':'announcement'})
        self.assertFalse(form.is_valid())

class Cooment_Form_Test(TestCase):

    def test_CommentForm_valid(self):
        form = CommentForm(data={
        'body':"I love the post bruh"
        })
        self.assertTrue(form.is_valid())

    def Test_CommentForm_invalid(self):
        form = CommentFOrm(data={})
        self.assertFalse(form.is_valid())

class User_Form_Test(TestCase):

    #Valid form data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': "user@mp.com", 'password': "user",
         'first_name': "user"})
        self.assertTrue(form.is_valid())
    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
