from django.test import TestCase, RequestFactory
from django.urls import reverse
from players.models import Player
from teams.models import Team
from matches.models import Match
from stats.models import Stat
from lavava.views import HomeView
from utils import calc_kda, calc_win_ratio


class HomeViewTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.player = Player.objects.create(username="Test Player")
        self.team = Team.objects.create()
        self.match = Match.objects.create(winner=self.team)
        self.stat = Stat.objects.create(
            player=self.player,
            team=self.team,
            kills=10,
            deaths=2,
            assists=5,
            mvp=True,
            ace=True,
        )
        self.team.match = self.match
        self.team.full_clean()
        self.team.save()

    def test_home_view_loads_correct_template(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "lavava/home.html")

    def test_home_url(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_context(self):
        request = self.factory.get(reverse("home"))
        response = HomeView.as_view()(request)
        self.assertIn("players", response.context_data)
        players = response.context_data["players"]
        self.assertEqual(len(players), 1)
        player = players[0]
        self.assertEqual(player.points, 5)
        self.assertEqual(player.winratio, 100)
        self.assertEqual(player.kda, 7.5)
