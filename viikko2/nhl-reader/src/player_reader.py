import requests
from player import Player

class PlayerReader:
    def __init__(self, given_url):
        self.url = given_url

    def get_players(self):
        request = requests.get(self.url).json()
        players = []

        for player_dict in request:
            player = Player(player_dict)
            players.append(player)
        
        return players