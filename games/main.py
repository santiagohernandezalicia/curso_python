'''programa principal de games'''
import json 
from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import game_logic as gl



def main(archivo_torneo:str):
    '''funcion principal de games'''
    if archivo_torneo != "":
       with open(archivo_torneo, "r", encoding="utf8") as file:
            torneo = json.load(file)
    else:
       g.create_gamefile()

    #jugar todos los juegos del torneo
    for juego in torneo:
        g.play_game(torneo)
    #calcular el tablero de puntuación
        juego = gl.json_to_game(juego)
        tablero = gl.scoring(torneo)
    gl.display_tablero(tablero)
    

if __name__ == "__main__":
    archivo_torneo = "torneo.json"
    main(archivo_torneo)