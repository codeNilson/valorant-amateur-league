from django.test import TestCase


class BlockAllauthURLsMiddlewareTest(TestCase):

    def test_block_allauth_urls_middleware_raises_http404_for_blocked_paths(self):
        blocked_paths = [
            "/accounts/password/reset/",
            "/accounts/password/change/",
            "/accounts/confirm-email/",
            "/accounts/password/reset/done/",
            "/accounts/password/reset/key/<uidb64>/<key>/",
            "/accounts/password/reset/key/done/",
            "/accounts/password/change/",
            "/accounts/email/",
        ]

        for blocked_path in blocked_paths:
            response = self.client.get(blocked_path)
            self.assertEqual(response.status_code, 404)
