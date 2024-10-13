def update_form_fields(form, field, css_class=None, **kwargs):
    field = form.fields.get(field)
    if css_class:
        old_classes = field.widget.attrs.get("class", "")
        new_classes = f"{old_classes} {css_class}".strip()
        field.widget.attrs.update({"class": new_classes})
    for attr, value in kwargs.items():
        field.widget.attrs.update({attr: value})
