from django.test import TestCase
from django.core.exceptions import ValidationError
from stats.models import Stat
from teams.models import Team
from players.models import Player
from gamedata.models import Agent


class TestStatModel(TestCase):

    def test_stats_get_kda_method(self):
        """Test the get_kda method of the Stat model."""

        # Test the case where the player has deaths
        stat = Stat(kills=10, deaths=5, assists=5)
        self.assertEqual(stat.get_kda(), 3.0)

        # Test the case where the player has no deaths
        stat = Stat(kills=10, deaths=0, assists=5)
        self.assertEqual(stat.get_kda(), 15.0)

        # Test the case where the player has no kills or assists
        stat = Stat()
        self.assertEqual(stat.get_kda(), None)

    def test_stats_clean_players_method(self):
        """Test the clean_players method of the Stat model."""

        # Create a team with 5 players
        team = Team.objects.create()
        for i in range(5):
            player = Player.objects.create_user(
                username=f"player{i}", password="password"
            )
            Stat.objects.create(player=player, team=team)

        with self.assertRaises(
            ValidationError,
            msg="The team 'team5 players.",
        ) as cm:
            # Try to add a new player to the team
            player = Player.objects.create(username="new_player", password="password")
            stat = Stat(player=player, team=team)
            stat.full_clean()

        # Try to add a player to a team with less than 5 players
        # team = Team.objects.create()
        # player = Player.objects.create()
        # stat = Stat(player=player, team=team)
        # stat.clean_players()
