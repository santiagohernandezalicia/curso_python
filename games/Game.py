from Athlete import Athlete
from Sport import Sport
from Team import Team

class Game:
    """Clase para representar un juego"""
    sport_dict = {
        'LMP': [x for x in range(1, 10)],
        'NBA': [x for x in range(70, 120)],
        'NFL': [x for x in range(3, 56)],
        'LMX': [x for x in range(0, 9)],
        'MLB': [x for x in range(0, 10)]
    }

    def __init__(self, A:Team, B:Team)-> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0
    
    def play(self):
        """juego simulado entre equipos"""
        for s in self.sport_dict.values():
            print(s)

if __name__ == "__main__":
    dt =['Jordan','Jhonson','Pipen','Bird','Kobe']
    cz =['Bjovik','Czak','Pfeizer','Leonard','Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basketball = Sport("NBA", 5, "DreamTeam")
    t = Team("Dream Team", basketball)
    c = Team("CzakTeam", basketball)
    game = Game(t, c)
    game.play()