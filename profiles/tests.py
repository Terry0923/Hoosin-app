from django.test import TestCase
from .models import Student, Club
from .forms import UserRegisterForm


# Create your tests here.
class StudentModelTests(TestCase):

    def test_student_object(self):
       s = Student(name="Gautam", year="fourth", major="Computer Engineering")
       self.assertEqual(s.name, "Gautam")
       self.assertEqual(s.year, "fourth")
       self.assertEqual(s.major, "Computer Engineering")


class ClubModelTests(TestCase):

    def test_club_object(self):
       c = Club(name="ACM", description="club for nerds")
       self.assertEqual(c.name, "ACM")
       self.assertEqual(c.description, "club for nerds")
