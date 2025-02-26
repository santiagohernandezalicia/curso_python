from Athlete import Athlete
from Sport import Sport
from Team import Team
from random import choice

class Game:
    """Clase para representar un juego"""
    sport_dict = {
        'LMP': [x for x in range(1, 10)],
        'NBA': [x for x in range(70, 120)],
        'NFL': [x for x in range(3, 56)],
        'LMX': [x for x in range(0, 9)],
        'MLB': [x for x in range(0, 10)],
        'FIFA': [x for x in range(0, 11)]
    }

    def __init__(self, A:Team, B:Team)-> None:
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0
    
    def play(self):
        """juego simulado entre equipos"""
        league = self.A.sport.league
        points= self.sport_dict[league]
        a = choice(points)
        b = choice(points)
        self.score[self.A.name] = a
        self.score[self.B.name] = b

    def __str__(self) -> str:
        """metodo para mostrar clase como string"""
        return f"Game: {self.A.name}: {self.score[self.A.name]} - {self.score[self.B.name]}:{self.B.name}"
    

    def __repr__(self) -> str:
        ''' metodo para representar la clase como string'''
        return f"Game(A={repr(self.A)}, B={repr(self.B)}"
    
    def to_json(self) -> dict:
        '''metodo para representar la clase como diccionarios'''
        return {"A": self.A.to_json(), "B": self.B.to_json(), "score": self.score}


if __name__ == "__main__":
    dt =['Jordan','Jhonson','Pipen','Bird','Kobe']
    cz =['Bjovik','Czak','Pfeizer','Leonard','Kempfe']
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basketball = Sport("DreamTeam",5,"NBA")
    t = Team("Dream Team", basketball,players_a)
    c = Team("CzakTeam", basketball,players_b)
    game = Game(t, c) 
    print(game)
    game.play()
    print(game)
    print(repr(game))
    print("--------")
    print(game.to_json())