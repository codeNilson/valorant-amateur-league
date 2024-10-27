from django.test import TestCase
from players.forms import PlayerLoginForm


class PlayerLoginFormTestCase(TestCase):
    def setUp(self):
        self.form = PlayerLoginForm()

    def test_login_field_has_correct_css_class(self):
        field = self.form.fields["login"]
        self.assertIn(
            "form-control border-0 bg-transparent", field.widget.attrs.get("class", "")
        )

    def test_login_field_has_autofocus(self):
        field = self.form.fields["login"]
        self.assertTrue(field.widget.attrs.get("autofocus", False))

    def test_password_field_has_correct_css_class(self):
        field = self.form.fields["password"]
        self.assertIn(
            "form-control border-0 bg-transparent", field.widget.attrs.get("class", "")
        )
