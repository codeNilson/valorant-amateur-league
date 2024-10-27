from django.test import TestCase
from players.forms import PlayerSignupForm


class PlayerSignupFormTestCase(TestCase):
    def setUp(self):
        self.form = PlayerSignupForm()

    def test_username_field_has_correct_css_class(self):
        field = self.form.fields["username"]
        self.assertIn(
            "form-control border-0 bg-transparent", field.widget.attrs.get("class", "")
        )

    def test_username_field_has_autofocus(self):
        field = self.form.fields["username"]
        self.assertTrue(field.widget.attrs.get("autofocus", False))

    def test_email_field_has_correct_css_class(self):
        field = self.form.fields["email"]
        self.assertIn(
            "form-control border-0 bg-transparent", field.widget.attrs.get("class", "")
        )

    def test_password1_field_has_correct_css_class(self):
        field = self.form.fields["password1"]
        self.assertIn(
            "form-control border-0 bg-transparent", field.widget.attrs.get("class", "")
        )

    def test_password2_field_has_correct_css_class(self):
        field = self.form.fields["password2"]
        self.assertIn(
            "form-control border-0 bg-transparent", field.widget.attrs.get("class", "")
        )
