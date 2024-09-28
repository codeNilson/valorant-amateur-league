from django.views import View
from django.shortcuts import render


class LandingPage(View):
    def get(self, request):
        return render(
            request,
            "lavava/landing_page.html",
        )
