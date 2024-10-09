from django.test import TestCase
from django.urls import reverse, resolve
from lavava.views import LandingPageView, HomeView


class LavavaUrlTests(TestCase):

    def test_landing_page_loads_correct_function(self):
        url = reverse("landing_page")
        response = resolve(url)
        self.assertEqual(response.func.view_class, LandingPageView)

    def test_landing_page_namespace(self):
        url = reverse("landing_page")
        self.assertEqual(url, "/")

    def test_home_namespace(self):
        url = reverse("home")
        self.assertEqual(url, "/home/")

    def test_home_loads_correct_function(self):
        url = reverse("home")
        response = resolve(url)
        self.assertEqual(response.func.view_class, HomeView)
