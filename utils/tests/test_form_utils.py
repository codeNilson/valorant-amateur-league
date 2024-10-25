from django import forms
from django.test import SimpleTestCase
from utils.forms_utils import update_form_fields


class SampleForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


class UpdateFormFieldsTests(SimpleTestCase):

    def test_update_form_fields_add_css_class(self):
        form = SampleForm()
        update_form_fields(form, "name", css_class="new-class")
        self.assertIn("new-class", form.fields["name"].widget.attrs["class"])

    def test_update_form_fields_add_multiple_css_classes(self):
        form = SampleForm()
        form.fields["name"].widget.attrs["class"] = "existing-class"
        update_form_fields(form, "name", css_class="new-class")
        self.assertEqual(
            "existing-class new-class", form.fields["name"].widget.attrs["class"]
        )

    def test_update_form_fields_add_custom_attribute(self):
        form = SampleForm()
        update_form_fields(form, "email", placeholder="Enter your email")
        self.assertEqual(
            "Enter your email", form.fields["email"].widget.attrs["placeholder"]
        )

    def test_update_form_fields_add_multiple_custom_attributes(self):
        form = SampleForm()
        update_form_fields(form, "name", placeholder="Enter your name", maxlength="50")
        self.assertEqual(
            "Enter your name", form.fields["name"].widget.attrs["placeholder"]
        )
        self.assertEqual("50", form.fields["name"].widget.attrs["maxlength"])

    def test_update_form_fields_no_existing_class(self):
        form = SampleForm()
        update_form_fields(form, "name", css_class="new-class")
        self.assertEqual("new-class", form.fields["name"].widget.attrs["class"])

    def test_update_form_fields_overwrite_existing_attribute(self):
        form = SampleForm()
        form.fields["email"].widget.attrs["placeholder"] = "Old placeholder"
        update_form_fields(form, "email", placeholder="New placeholder")
        self.assertEqual(
            "New placeholder", form.fields["email"].widget.attrs["placeholder"]
        )
