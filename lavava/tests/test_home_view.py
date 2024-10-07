from django.test import TestCase
from django.urls import reverse


class LandingPageViewTests(TestCase):
    def test_home_view_loads_correct_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "lavava/home.html")

    def test_home_url(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
