#test cases for Models

from django.test import TestCase
from .models import Student, Club, Profile
from .forms import UserRegisterForm
from django.contrib.auth.models import User
# Create your tests here.
#test for models
class StudentModelTest(TestCase):

    def test_student_object(self):
       s = Student(name="Gautam", year="fourth", major="Computer Engineering")
       self.assertEqual(s.name, "Gautam")
       self.assertEqual(s.year, "fourth")
       self.assertEqual(s.major, "Computer Engineering")


class ClubModelTest(TestCase):

    def test_club_object(self):
       c = Club(name="ACM", description="club for nerds")
       self.assertEqual(c.name, "ACM")
       self.assertEqual(c.description, "club for nerds")

class DefaultUserModelTest(TestCase):

    def test_User_object(self):
        user = User(username="terry",email="jt2fx@virginia.edu")
        self.assertEqual(user.username, "terry")
        self.assertEqual(user.email,"jt2fx@virginia.edu")

class ProfileModelTest(TestCase):

    def test_profile_creation(self):
        profile = Profile(year="third year",major="Computer Science")
        isinstance(profile, Profile)
#       self.assertEqual(profile.__str__(), profile.year)



class ProfileSetupModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create()

    def test_user_is_created(self):
        self.assertTrue(User.objects.count() == 1)



        '''
class RegisterFormTests(TestCase):
self.user.username
    def test_registration_class(self):
        register = UserRegisterForm(email="jt2fx@company.edu")
        self.assertRaises(ValidationError, register.email)
        '''
