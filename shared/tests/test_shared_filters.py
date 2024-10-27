from django.test import TestCase
from shared.templatetags.form_utils import field_icon


class FieldIconFilterTestCase(TestCase):
    def test_field_icon_returns_user_icon_for_username(self):
        result = field_icon("username")
        self.assertEqual(result, "<i class='fa-solid fa-user'></i>")

    def test_field_icon_returns_email_icon_for_email(self):
        result = field_icon("email")
        self.assertEqual(result, "<i class='fa-solid fa-envelope'></i>")

    def test_field_icon_returns_lock_icon_for_password1(self):
        result = field_icon("password1")
        self.assertEqual(result, "<i class='fa-solid fa-lock'></i>")

    def test_field_icon_returns_lock_icon_for_password2(self):
        result = field_icon("password2")
        self.assertEqual(result, "<i class='fa-solid fa-lock'></i>")

    def test_field_icon_returns_agent_icon_for_main_agent(self):
        result = field_icon("main_agent")
        self.assertEqual(result, "<i class='fa-solid fa-mask'></i>")

    def test_field_icon_returns_medal_icon_for_tier(self):
        result = field_icon("tier")
        self.assertEqual(result, "<i class='fa-solid fa-medal'></i>")

    def test_field_icon_returns_empty_string_for_nonexistent_field(self):
        result = field_icon("nonexistent_field")
        self.assertEqual(result, "")
