from django.test import TestCase
from django.contrib.auth import get_user_model
from matches.models import Match
from teams.models import Team
from stats.models import Stat
from ..templatetags.matches import get_embed_url


class MatchHistoryTagTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        self.match = Match.objects.create()
        self.team = Team.objects.create(match=self.match)
        self.stat = Stat.objects.create(team=self.team, player=self.user, mvp=True)
        self.client.login(username="testuser", password="12345")


class GetEmbedUrlFilterTest(TestCase):
    def test_get_embed_url_transforms_url(self):
        youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        expected_embed_url = "https://www.youtube.com/embed/dQw4w9WgXcQ"
        self.assertEqual(get_embed_url(youtube_url), expected_embed_url)
