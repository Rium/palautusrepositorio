import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        players = [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "team": "AAA",
                "goals": 10,
                "assists": 20,
            }),
            Player({
                "name": "Player Two",
                "nationality": "FIN",
                "team": "BBB",
                "goals": 15,
                "assists": 10,
            }),
            Player({
                "name": "Player Three",
                "nationality": "SWE",
                "team": "AAA",
                "goals": 20,
                "assists": 5,
            }),
        ]
        self.stats = PlayerStats(PlayerReaderStub(players))

    def test_top_scorers_by_nationality(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player[1][0] for player in players],
                         ["Player One", "Player Two"])

    def test_top_scorers_by_team(self):
        players = self.stats.top_scorers_by_team("AAA")

        self.assertEqual([player[1][0] for player in players],
                         ["Player One", "Player Three"])

    def test_top_goal_scorers(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual([player[1][0] for player in players],
                         ["Player Three", "Player Two"])


if __name__ == "__main__":
    unittest.main()