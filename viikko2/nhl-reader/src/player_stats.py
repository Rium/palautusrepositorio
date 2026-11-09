class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self.players:
            data = player.data()
            if data[1] == nationality:
                players.append([player, data])

        top_score = sorted(players, key=lambda score: score[1][5], reverse=True)

        return top_score

    def top_scorers_by_team(self, team):
        players = []

        for player in self.players:
            data = player.data()
            if data[2] == team:
                players.append([player, data])

        top_score = sorted(players, key=lambda score: score[1][5], reverse=True)

        return top_score

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        players = []

        for player in self.players:
            data = player.data()
            players.append([player, data])

        top_score = sorted(players, key=lambda score: score[1][3], reverse=True)

        return top_score[:how_many]
        # lol nope, tosin ymmärrettävää kattoen miten toteutin ton edellisen. Ei se tiedä mitä tuolla datassa on sisällä.
        # Agentti korjasi tämän hienosti, aikasempi toteutus oli siis "score[1][5]"