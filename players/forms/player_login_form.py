from allauth.account.forms import LoginForm
from utils.forms_utils import update_form_fields


class PlayerLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        update_form_fields(self, "login", css_class="form-control", autofocus=True)
        update_form_fields(self, "password", css_class="form-control")
        update_form_fields(self, "remember", css_class="form-check-input")
