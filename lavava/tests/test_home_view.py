from django.test import TestCase
from django.urls import reverse
from players.models import Player


class HomeViewTests(TestCase):

    def setUp(self):
        # Configurar dados de teste
        self.player1 = Player.objects.create(username="Player 1")
        self.player2 = Player.objects.create(username="Player 2")

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
        self.assertIn("players", response.context)
        players = response.context["players"]
        self.assertEqual(len(players), 2)
        self.assertEqual(players[0].username, "Player 1")
        self.assertIn("update_at", response.context)

    def test_home_view_post_method_redirect_to_home(self):
        url = reverse("home")
        response = self.client.post(url, follow=True)
        self.assertRedirects(response, url)

    def test_home_view_post_saves_position_changes(self):
        url = reverse("home")
        self.client.post(url, follow=True)
        self.player1.refresh_from_db()
        self.player2.refresh_from_db()
        self.assertEqual(self.player1.rankinglog.last_position, 1)
        self.assertEqual(self.player1.rankinglog.last_position_change, -1)
        self.assertEqual(self.player2.rankinglog.last_position, 2)
        self.assertEqual(self.player2.rankinglog.last_position_change, -2)
