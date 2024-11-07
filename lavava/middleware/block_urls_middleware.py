from django.http import Http404


class BlockAllauthURLsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        blocked_paths = [
            "/accounts/password/reset/",
            "/accounts/password/change/",
            "/accounts/confirm-email/",
            "/accounts/password/reset/done/",
            "/accounts/password/reset/key/<uidb64>/<key>/",
            "/accounts/password/reset/key/done/",
            "/accounts/password/change/",
            "/accounts/email/",
            "/accounts/login/",
            "/accounts/signup/",
            "/accounts/logout/",
        ]

        if request.path in blocked_paths:
            raise Http404("Allauth URLs are blocked")

        return self.get_response(request)
