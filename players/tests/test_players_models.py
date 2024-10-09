from django.test import TestCase
from django.db.models import F
from players.models import Player
from teams.models import Team
from stats.models import Stat
from gamedata.models import Tier, Agent
from matches.models import Match


class PlayerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Setup initial data for the tests
        cls.tier = Tier.objects.create(tier="Gold")
        cls.agent = Agent.objects.create(name="Jett")
        cls.player = Player.objects.create_user(
            username="jhon_doe",
            password="password",
            tier=cls.tier,
            main_agent=cls.agent,
        )
        cls.team = Team.objects.create()
        cls.team2 = Team.objects.create()
        cls.team3 = Team.objects.create()

        # Create a match
        match = Match.objects.create(winner=cls.team)
        match2 = Match.objects.create(winner=cls.team3)

        # Create stats for the player
        Stat.objects.create(
            player=cls.player,
            team=cls.team,
            kills=10,
            deaths=5,
            assists=2,
            mvp=True,
            ace=False,
        )
        Stat.objects.create(
            player=cls.player,
            team=cls.team2,
            kills=8,
            deaths=3,
            assists=1,
            mvp=False,
            ace=True,
        )

    def test_annotate_wins_and_losses(self):
        queryset = Player.objects.all()
        annotated_queryset = Player.annotate_wins_and_losses(queryset)
        player = annotated_queryset.first()
        self.assertEqual(player.wins, 1)
        self.assertEqual(player.losses, 1)

    def test_annotate_mvp_and_ace(self):
        queryset = Player.objects.all()
        annotated_queryset = Player.annotate_mvp_and_ace(queryset)
        player = annotated_queryset.first()
        self.assertEqual(player.mvp, 1)
        self.assertEqual(player.ace, 1)

    def test_annotate_kills_deaths_assists(self):
        queryset = Player.objects.all()
        annotated_queryset = Player.annotate_kills_deaths_assists(queryset)
        player = annotated_queryset.first()
        self.assertEqual(player.total_kills, 18)
        self.assertEqual(player.total_deaths, 8)
        self.assertEqual(player.total_assists, 3)

    def test_annotate_points(self):
        queryset = Player.objects.all()
        annotated_queryset = Player.annotate_mvp_and_ace(queryset)
        annotated_queryset = Player.annotate_wins_and_losses(annotated_queryset)
        annotated_queryset = Player.annotate_points(annotated_queryset)
        player = annotated_queryset.first()
        self.assertEqual(player.points, 5)  # 1 MVP + 1 ACE + 1 Wins * 3

    def test_annotate_kda(self):
        # Caso com total_deaths diferente de 0
        queryset = Player.objects.all()
        annotated_queryset = Player.annotate_kills_deaths_assists(queryset)
        annotated_queryset = Player.annotate_kda(annotated_queryset)
        player = annotated_queryset.first()
        expected_kda = (18 + 3) / 8  # (total_kills + total_assists) / total_deaths
        self.assertAlmostEqual(player.kda, expected_kda, places=2)

        # Caso com total_deaths igual a 0
        player_with_no_deaths = Player.objects.create_user(
            username="no_deaths_player",
            password="password",
            tier=self.tier,
            main_agent=self.agent,
        )
        Stat.objects.create(
            player=player_with_no_deaths,
            team=self.team,
            kills=10,
            deaths=0,
            assists=5,
            mvp=False,
            ace=False,
        )

        queryset = Player.objects.filter(username="no_deaths_player")
        annotated_queryset = Player.annotate_kills_deaths_assists(queryset)
        annotated_queryset = Player.annotate_kda(annotated_queryset)
        player = annotated_queryset.first()
        expected_kda = 10 + 5  # total_kills + total_assists
        self.assertAlmostEqual(player.kda, expected_kda, places=2)

    def test_annotate_win_ratio(self):
        queryset = Player.objects.all()
        annotated_queryset = Player.annotate_wins_and_losses(queryset)
        annotated_queryset = Player.annotate_win_ratio(annotated_queryset)
        player = annotated_queryset.first()
        self.assertEqual(player.win_ratio, 50.0)
