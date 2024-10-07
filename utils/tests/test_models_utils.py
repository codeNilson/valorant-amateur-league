from unittest import TestCase
from utils import calc_kda, calc_win_ratio


class ModelsUtilsTestCase(TestCase):
    def test_calc_kda(self):
        kills = 10
        assists = 5
        deaths = 2
        kda = calc_kda(kills, assists, deaths)
        self.assertEqual(kda, 7.5)

        kills = 0
        assists = 0
        deaths = 0
        kda = calc_kda(kills, assists, deaths)
        self.assertEqual(kda, 0)

        kills = 10
        assists = 5
        deaths = 0
        kda = calc_kda(kills, assists, deaths)
        self.assertEqual(kda, 15)

        kills = 10
        assists = 0
        deaths = 2
        kda = calc_kda(kills, assists, deaths)
        self.assertEqual(kda, 5)

        kda = calc_kda()
        self.assertEqual(kda, 0)

    def test_get_kda(self):
        wins = 10
        losses = 5
        win_ratio = calc_win_ratio(wins, losses)
        self.assertEqual(win_ratio, 66.67)

        wins = 0
        losses = 0
        win_ratio = calc_win_ratio(wins, losses)
        self.assertEqual(win_ratio, 0)

        wins = 10
        losses = 0
        win_ratio = calc_win_ratio(wins, losses)
        self.assertEqual(win_ratio, 100)

        wins = 0
        losses = 5
        win_ratio = calc_win_ratio(wins, losses)
        self.assertEqual(win_ratio, 0)

        win_ratio = calc_win_ratio()
        self.assertEqual(win_ratio, 0)
