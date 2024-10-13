from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "text-bg-info border-info",
    messages.INFO: "text-bg-info border-info",
    messages.SUCCESS: "text-bg-success border-success",
    messages.WARNING: "text-bg-warning border-warning",
    messages.ERROR: "text-bg-danger border-danger",
}
