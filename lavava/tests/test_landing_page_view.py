from django.test import TestCase
from django.urls import reverse


class LandingPageViewTests(TestCase):
    def test_landing_page_view_loads_correct_template(self):
        url = reverse("landing_page")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "lavava/landing_page.html")

    def test_landing_page_url(self):
        url = reverse("landing_page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
