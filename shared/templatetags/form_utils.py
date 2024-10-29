from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()

ICON_MAP = {
    "username": "fa-user",
    "email": "fa-envelope",
    "password1": "fa-lock",
    "password2": "fa-lock",
    "main_agent": "fa-mask",
    "tier": "fa-medal",
}


@register.filter(is_safe=True)
@stringfilter
def field_icon(value):
    icon_class = ICON_MAP.get(value)
    if icon_class:
        return mark_safe(f"<i class='fa-solid {icon_class}'></i>")
    return ""
