from django import forms
from players.models import Player
from utils.forms_utils import update_form_fields


class PlayerModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_form_fields(
            self,
            "username",
            css_class="form-control border-0 bg-transparent",
            autofocus=True,
        )
        update_form_fields(
            self,
            "email",
            css_class="form-control border-0 bg-transparent",
        )
        update_form_fields(
            self,
            "main_agent",
            css_class="form-control border-0 bg-transparent",
        )
        update_form_fields(
            self,
            "include_in_draft",
            css_class="form-check-input",
            label="I want to be included in the draft",
        )

    class Meta:
        model = Player
        fields = [
            "username",
            "email",
            "main_agent",
            "include_in_draft",
        ]
