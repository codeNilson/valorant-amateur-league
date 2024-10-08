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
        url = reverse("home")
        response = self.client.get(url)
        self.assertIn("players", response.context_data)
        players = response.context_data["players"]
        self.assertEqual(len(players), 1)
        player = players[0]
        self.assertEqual(player.points, 5)
        self.assertEqual(player.winratio, 100)
        self.assertEqual(player.kda, 7.5)

    def test_home_view_post_method_redirect_to_home(self):
        url = reverse("home")
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, url)

    def test_home_view_post_method_successfully_updates_player_position(self):
        self.assertEqual(self.player.last_position, 0)
        self.assertEqual(self.player.last_position_change, 0)
        self.assertEqual(self.player.get_position_class(), "fa-minus")

        url = reverse("home")
        self.client.post(url, follow=True)
        self.assertEqual(self.player.last_position, 1)
        self.assertEqual(self.player.last_position_change, 1)
        self.assertEqual(self.player.get_position_class(), "fa-caret-up")
