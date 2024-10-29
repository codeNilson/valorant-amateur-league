from django.test import TestCase
from matches.models import Match
from teams.models import Team
from gamedata.models import Map
from django.core.exceptions import ValidationError


class TestMatchesModel(TestCase):

    fixtures = ["gamedata/fixtures/gamedata_fixtures.json"]

    def setUp(self) -> None:

        self.map = Map.objects.all().first()
        self.match = Match.objects.create(map=self.map)
        self.team = Team.objects.create(match=self.match)
        self.team2 = Team.objects.create()

        return super().setUp()

    def test_clean_winner(self):

        with self.assertRaises(ValidationError):
            self.match.winner = self.team2
            self.match.full_clean()

    def test_clean(self):

        with self.assertRaises(ValidationError):
            self.match.winner = self.team2
            self.match.clean()
