from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, PlayerReader):
        self.players = PlayerReader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self.players:
            data = player.data() 
            if data[1] == nationality: players.append([player, data])

        top_score = sorted(players, key=lambda score: score[1][5], reverse=True)
        """return_list = []

        for player in top_score:
            return_list.append(player[0])

        return return_list"""
        return top_score
    