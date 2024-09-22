from django.forms import ValidationError
from django.test import TestCase
from teams.models import Team
from matches.models import Match


class TeamsModelTest(TestCase):
    def test_teams_model_clean(self):
        match = Match.objects.create()
        with self.assertRaises(ValidationError):
            for i in range(4):
                team = Team.objects.create(match=match)
                team.full_clean()  # Aqui o save acionará a validação e levantará o erro
