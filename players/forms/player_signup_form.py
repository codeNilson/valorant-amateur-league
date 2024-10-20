from allauth.account.forms import SignupForm
from utils.forms_utils import update_form_fields


class PlayerSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_form_fields(
            self,
            "username",
            css_class="form-control border-0 bg-transparent",
            autofocus=True,
        )
        update_form_fields(
            self, "email", css_class="form-control border-0 bg-transparent"
        )
        update_form_fields(
            self, "password1", css_class="form-control border-0 bg-transparent"
        )
        update_form_fields(
            self, "password2", css_class="form-control border-0 bg-transparent"
        )
