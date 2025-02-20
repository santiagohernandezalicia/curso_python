import json
class Sport:
    '''clase para representar un deporte'''
    def __init__(self, name:str, players:int, league:str):
        '''constructor de sport'''
        self.name = name
        if isinstance(players, int): # si players es un entero  
            self.players = players
        else:
            self.players = int(players) # si no lo convierte a entero
        self.league = league

    def __str__ (self)-> str:
        '''representacion en string de sport'''
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self)-> str:
        '''representacion en string de sport'''
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self)-> dict:
        '''Convertir sport a json'''
        return {"name": self.name, "players": self.players, "league": self.league}

if __name__ == "__main__":
    s = Sport("Soccer", 11, "FIFA")
    print(s)
    print(repr(s))
    print(s.to_json())
    nfl= Sport("Football", "11", "NFL")
    lmp = Sport("Baseball", "9", "LMP")
    mlb = Sport("Baseball", 9, "MLB")
    lmx = Sport("Soccer", 11, "Liga MX")
    nba = Sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba, s]
    #Salvamos objetos como texto (su representacion)
    archivo_deportes = "deportes.txt"
    with open(archivo_deportes, "w") as file:
          for d in lista_deportes:
            file.write(repr(d)+ "\n")
    sport_list =[]
    with open(archivo_deportes, "r") as file:
        for line in file:
            d = eval(line)
            sport_list.append(d)
    print(sport_list)
    print(sport_list[0].to_json())
    #Escribimos el archivo en formato json
    archivo_json = "deportes.json"
    #convert all sport to json
    sport_json = [s.to_json() for s in sport_list]
    #write the entire list a single json array
    with open(archivo_json, "w") as file:
        json.dump(sport_json, file, indent=4)
    
    #Leemos el archivo json
    sport_list_json = []
    with open(archivo_json, "r") as file:
        sport_list_json = json.load(file)
    print(sport_list_json)