from django.forms import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model
from teams.models import Team
from matches.models import Match


class TeamsModelTest(TestCase):
    def test_teams_models_raises_an_error_if_three_teams_are_associated(self):

        # Create a Match instance
        match = Match.objects.create()

        # Create two Team instances and associate them with the Match instance
        for _ in range(2):
            Team.objects.create(match=match)

        # Create a third Team instance and associate it with the Match instance
        with self.assertRaises(ValidationError) as cm:
            third_team = Team(match=match)
            third_team.full_clean()

        error = cm.exception

        self.assertIn("A match cannot have more than two teams", error.messages)

    def test_teams_model_get_players_method(self):
        team = Team.objects.create()
        self.assertEqual(list(team.get_players()), [])

        player_model = get_user_model()
        player = player_model.objects.create_user(
            username="jhon_doe", password="password"
        )
        team.players.add(player)
        self.assertEqual(list(team.get_players()), [player])

    def test_teams_model_get_players_performance_method(self):

        team = Team.objects.create()
        self.assertEqual(list(team.get_players_perfomance()), [])

        player_model = get_user_model()
        player = player_model.objects.create_user(
            username="jhon_doe", password="password"
        )
        team.players.add(player)
        self.assertEqual(
            list(team.get_players_perfomance()),
            [player.stats.filter(team=team).first()],
        )

    def test_team_model_str_method(self):
        team = Team.objects.create()
        self.assertEqual(str(team), str(team.uuid))
