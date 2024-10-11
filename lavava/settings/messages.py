from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: "text-bg-info border-info alert-dismissible fade show",
    messages.INFO: "text-bg-info border-info alert-dismissible fade show",
    messages.SUCCESS: "text-bg-success border-success alert-success alert-dismissible fade show",
    messages.WARNING: "text-bg-warning border-warning alert-dismissible fade show",
    messages.ERROR: "text-bg-red border-danger alert-dismissible fade show",
}
