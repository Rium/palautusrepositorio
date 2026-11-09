class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
        self.score = self.goals + self.assists

    def data(self):
        return [self.name, self.nationality, self.team, self.goals, self.assists, self.score]
    
    def __str__(self):
        return f"{self.name:20} {self.team:20} {self.goals} + {self.assists} = {self.score}"
