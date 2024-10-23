from django import template

register = template.Library()

ICON_MAP = {
    "username": "fa-user",
    "email": "fa-envelope",
    "password1": "fa-lock",
    "password2": "fa-lock",
    "main_agent": "fa-mask",
    "tier": "fa-medal",
}


@register.filter
def field_icon(value):
    icon_class = ICON_MAP.get(value)
    if icon_class:
        return f"<i class='fa-solid {icon_class}'></i>"
    return ""
