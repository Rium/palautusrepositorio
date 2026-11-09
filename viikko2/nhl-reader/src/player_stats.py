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