class Player:
    def __init__(self, p_dict):
        self.name = p_dict['name']
        self.team = p_dict['team']
        self.goals = p_dict['goals']
        self.assists = p_dict['assists']
        self.nationality = p_dict['nationality']
        self.score = self.goals + self.assists

    def data(self):
        return [self.name, self.nationality, self.team, self.goals, self.assists, self.score]

    def __str__(self):
        return f"{self.name:20} {self.team:20} {self.goals} + {self.assists} = {self.score}"