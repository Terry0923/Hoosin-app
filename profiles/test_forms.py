#test cases for forms.py

from django.test import TestCase
from django.test import Client
from .forms import UserRegisterForm
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
'''
class UserCreationFormTest(TestCase):

    def test_user_email_form(self):
        data = {
            'email':'jt2fx@virginia.edu'
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())


class Setup_Class(TestCase):


    def setUp(self):
        self.user = User.objects.create(email="terry@virgina.edu")


class Register_Form_Test(TestCase):

    def test_RegisterForm_invalid(self):
        form = UserRegisterForm(data={
        'email': "terry@virginia.edu"
        })
        self.assertTrue(form.is_valid())

    def test_RegisterForm_valid(self):
        form = UserRegisterForm(data={
        'email': "terry@virginia.edu",
        'first_name': "Terry",
        'last_name':"Tsai"
        })
        self.assertTrue(form.is_valid())
'''
