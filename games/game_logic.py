''' Lógica de la puntuación del juego '''
import json
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game

def add_team_to_score(team:str, score:dict):
    ''' Agrega un equipo al diccionario de puntuación '''
    if team not in score:
        score[team] = {
            'G':0,
            'E':0,
            'P':0
        }

def scoring(torneo:list)->dict:
    ''' Puntuación de juegos'''
    tablero = {}
    for juego in torneo:
        equipo_local = juego["A"]["name"]
        equipo_visitante = juego["B"]["name"]
        if equipo_local not in tablero:
            add_team_to_score(equipo_local, tablero)
        if equipo_visitante not in tablero:
            add_team_to_score(equipo_visitante, tablero)
    for juego in torneo:
        equipo_local = juego["A"]["name"]
        equipo_visitante = juego["B"]["name"]
        goles_local = juego["score"][equipo_local]
        goles_visitante = juego["score"][equipo_visitante]
        if goles_local > goles_visitante:
            tablero[equipo_local]['G'] += 1
            tablero[equipo_visitante]['P'] += 1
        elif goles_local < goles_visitante:
            tablero[equipo_local]['P'] += 1
            tablero[equipo_visitante]['G'] += 1
        else:
            tablero[equipo_local]['E'] += 1
            tablero[equipo_visitante]['E'] += 1
    return tablero

def display_tablero(tablero:dict):
    ''' Muestra el tablero de puntuación '''
    print("----------------")
    for equipo, puntaje in tablero.items():
        print(f"{equipo}: {puntaje['G']}G {puntaje['E']}E {puntaje['P']}P")
    print("----------------")
    print("Tabla de posiciones")
    tabla = sorted(tablero.items(), key=lambda x: x[1]['G'], reverse=True)
    for i, (equipo, puntaje) in enumerate(tabla, 1):
        print(f"{i}. {equipo}: {puntaje['G']}G {puntaje['E']}E {puntaje['P']}P")

def json_to_game(json:dict)->Game:
    ''' Convierte un diccionario en un objeto Game '''
    A = Team(json['A']['name'], 
             Sport(json['A']['sport']['name'],json['A']['sport']['players'], json['A']['sport']['league']), [Athlete(x['name']) for x in json['A']['players']])
    B = Team(json['B']['name'], 
             Sport(json['B']['sport']['name'], json['B']['sport']['players'], json['B']['sport']['league']),[Athlete(x['name']) for x in json['B']['players']])
    game = Game(A, B)  
    game.score = json['score']
    return game

def json_to_tournament(torneo:dict)->list:
    ''' Convierte el torneo en una lista de juegos'''
    return [json_to_game(juego) for juego in torneo]

def create_gamefile():
    ''' Crea un archivo de juegos '''
    players_mexico=['Chicharito','Chuky','Ochoa','Tecatito','Guardado','Herrera','Layun','Moreno','Araujo','Oribe','Jimenez']
    players_españa=['Casillas','Ramos','Pique','Iniesta','Silva','Isco','Busquets','Costa','Moreta','Ascensio']
    players_brazil=['Neymar','Coutinho','Marcelo','Casemiro','Alisson','Jesus','Paulinho','Thiago','Firmino','Danilo']
    players_argentina=['Messi','Aguero','Di Maria','Marcherano','Higuan','Dybala','Otamendi','Rojo','Banega','Perez']

    lista_mexico=[Athlete(x) for x in players_mexico]
    lista_españa=[Athlete(x) for x in players_españa]
    lista_brazil=[Athlete(x) for x in players_brazil]
    lista_argentina=[Athlete(x) for x in players_argentina]
    soccer = Sport("Soccer",11,"FIFA")
    mexico = Team("Mexico", soccer,lista_mexico)
    españa = Team("España", soccer,lista_españa)
    brazil = Team("Brazil", soccer,lista_brazil)
    argentina = Team("Argentina", soccer,lista_argentina)
    equipos = [mexico,españa,brazil,argentina]

    d={}
    for local in equipos:
        for visitante in equipos:
            if local != visitante:
                juego = Game(local,visitante)
                partido =f'{local} - {visitante}'
                partido_2 = f'{visitante} - {local}'
                if partido_2 not in d:
                    d[partido] = juego.to_json()
    torneo = list(d.values())

    #juego = Game(mexico,españa)
    #torneo = [juego.to_json()]
    archivo_torneo = "torneo.json"
    with open(archivo_torneo, "w", encoding="utf8") as f:
        json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"Archivo {archivo_torneo} creado")

def play_game(torneo:dict):
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
    
    game = Game(A, B)
    game.play()
    print(game)
    juego['score'] = game.score
    print("______________________________")

if __name__ == "__main__":
    archivo = "torneo.json"
    with open(archivo, "r") as f:
        torneo = json.load(f)
    tournament = json_to_tournament(torneo)
    for game in tournament:
        game.play()
    torneo = [game.to_json() for game in tournament]
    tablero = scoring(torneo)
    display_tablero(tablero)
    

 