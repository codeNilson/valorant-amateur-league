from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from stats.models import Stat
from teams.models import Team


class TestStatModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.player_model = get_user_model()
        cls.player = cls.player_model.objects.create_user(
            username="jhon_doe", password="password"
        )

        cls.team = Team.objects.create()

        cls.stat = Stat.objects.create(player=cls.player, team=cls.team)

    def test_stats_get_kda_method(self):

        # Test the case where the player has no kills or assists
        self.assertEqual(self.stat.get_kda(), None)

        # Test the case where the player has deaths
        self.stat.kills = 10
        self.stat.deaths = 2
        self.stat.assists = 5
        self.assertEqual(self.stat.get_kda(), 7.5)

        # Test the case where the player has no deaths
        self.stat.kills = 10
        self.stat.deaths = 0
        self.stat.assists = 5
        self.assertEqual(self.stat.get_kda(), 15.0)

    def test_stats_clean_players_method_raises_error_if_it_has_too_many_players(self):

        # Create a team with 5 players
        for i in range(5):
            player = self.player_model.objects.create_user(
                username=f"player{i}", password="password"
            )
            Stat.objects.create(player=player, team=self.team)

        # Test if a ValidationError is raised when trying to add a sixth player
        with self.assertRaises(ValidationError):
            stat = Stat(player=self.player, team=self.team)
            stat.full_clean()

    def test_stats_clean_players_methods_raises_error_if_player_is_already_in_team(
        self,
    ):

        # Create a team with 4 players
        for i in range(4):
            player = self.player_model.objects.create_user(
                username=f"player{i}", password="password"
            )
            Stat.objects.create(player=player, team=self.team)

        # Test if a ValidationError is raised when trying
        # to add a player that is already in the team
        with self.assertRaises(ValidationError) as cm:
            stat = Stat(player=player, team=self.team)
            stat.full_clean()

        error = cm.exception
        self.assertIn("Stat com este Player e Team já existe.", error.messages)

    def test_stats_str_method(self):

        # Test if the __str__ method returns the expected value
        self.assertEqual(str(self.stat), "jhon_doe")
