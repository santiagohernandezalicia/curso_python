'''programa principal de games'''
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json 

def main(archivo_torneo:str):
    '''funcion principal de games'''
    if archivo_torneo != "":
       with open(archivo_torneo, "r", encoding="utf8") as file:
            torneo = json.load(file)
    else:
        players_mexico=['Chicharito','Chuky','Ochoa','Tecatito','Guardado','Herrera','Layun','Moreno','Araujo','Oribe','Jimenez']
        players_españa=['Casillas','Ramos','Pique','Iniesta','Silva','Isco','Busquets','Costa','Moreta','Ascensio']
        lista_mexico=[Athlete(x) for x in players_mexico]
        lista_españa=[Athlete(x) for x in players_españa]
        soccer = Sport("Soccer",11,"FIFA")
        mexico = Team("Mexico", soccer,lista_mexico)
        españa = Team("España", soccer,lista_españa)
        juego = Game(mexico,españa)
        torneo = [juego.to_json()]
        archivo_torneo = "torneo.json"
        with open(archivo_torneo, "w", encoding="utf8") as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
            print(f"Archivo {archivo_torneo} creado")
        #jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)