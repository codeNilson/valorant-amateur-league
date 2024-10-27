from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from matches.models import Match
from teams.models import Team
from stats.models import Stat
from ..templatetags.matches import match_history, get_embed_url


class MatchHistoryTagTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        self.match = Match.objects.create()
        self.team = Team.objects.create(match=self.match)
        self.stat = Stat.objects.create(team=self.team, player=self.user, mvp=True)
        self.client.login(username="testuser", password="12345")

    def test_match_history_includes_matches(self):
        url = reverse("landing_page")
        response = self.client.get(url)
        context = response.context
        result = match_history(context)
        self.assertIn("matches", result)
        self.assertEqual(result["matches"].count(), 1)

    def test_match_history_filters_by_username(self):
        url = reverse("account_profile", kwargs={"username": self.user.username})
        response = self.client.get(url)

        context = response.context
        context["request"].resolver_match = type(
            "MockResolverMatch", (), {"kwargs": {"username": "testuser"}}
        )()

        result = match_history(context)

        self.assertEqual(result["matches"].count(), 1)
        self.assertEqual(result["matches"].first().mvp, "testuser")

    def test_match_history_does_not_filter_without_username(self):
        response = self.client.get("/")
        context = response.context
        context["request"].resolver_match = type("", (), {"kwargs": {}})()
        result = match_history(context)
        self.assertEqual(result["matches"].count(), 1)


class GetEmbedUrlFilterTest(TestCase):
    def test_get_embed_url_transforms_url(self):
        youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        expected_embed_url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        self.assertEqual(get_embed_url(youtube_url), expected_embed_url)
