import asyncio
import threading
import sys
import os
sys.path.append(os.path.abspath("src"))

from WebSocket.websocket_server import start_websocket_server
from Rover.rover import Rover

def lancer_websocket():
    asyncio.run(start_websocket_server())

def main():
    # Lancer le WebSocket dans un thread à part
    threading.Thread(target=lancer_websocket, daemon=True).start()

    planete = (10, 10)
    obstacles = [(3, 3), (5, 5), (7, 7)]
    rover = Rover(5, 5, 'N', planete, obstacles)

    print("Aujourd'hui vous êtes au contrôle de Rover !")
    print("Commandes : A = avancer, R = reculer, G = gauche, D = droite, S = séquence, Q = quitter")

    while True:
        commande = input("Commande : ").upper()
        if commande in ['A', 'R']:
            rover.deplacer(commande)
        elif commande in ['G', 'D']:
            rover.tourner(commande)
        elif commande == 'S':
            sequence = input("Séquence de commandes : ").upper()
            rover.executer_commandes(sequence)
        elif commande == 'Q':
            print("Au revoir depuis Mars !")
            break
        else:
            print("Commande invalide.")
            continue

        print(rover.get_position())
        rover.afficher_carte()

if __name__ == "__main__":
    main()
