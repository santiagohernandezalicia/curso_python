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
        #jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego['A']['name'], Sport(juego['A']['sport']['name'], juego['A']['sport']['players'], juego['A']['sport']['league']), [Athlete(x['name']) for x in juego['A']['players']])
        B = Team(juego['B']['name'], Sport(juego['B']['sport']['name'], juego['B']['sport']['players'], juego['B']['sport']['league']), [Athlete(x['name']) for x in juego['B']['players']])
        
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")

if __name__ == "__main__":
    archivo_torneo = "torneo.json"
    main(archivo_torneo)
