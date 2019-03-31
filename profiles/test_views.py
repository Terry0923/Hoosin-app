#Test cases for views
import unittest
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from . import views

class PageTest(TestCase):

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_logout_page_status_code(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)


    def test_student_page_status_code(self):
        response = self.client.get(reverse('profiles:student-index'))
        self.assertEquals(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

        #look into what status 302
    def test_profile_page_status_code(self):
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 302)

    def test_admin_page_status_code(self):
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 302)

    def test_club_page_status_code(self):
        response = self.client.get(reverse('profiles:club-index'))
        self.assertEquals(response.status_code, 200)

    def test_search_form_page_status_code(self):
        response = self.client.get(reverse('profiles:search-form'))
        self.assertEquals(response.status_code, 200)

    def test_search_results_page_status_code(self):
        response = self.client.get(reverse('profiles:search-results'))
        self.assertEquals(response.status_code, 200)
