import asyncio
import threading
import sys
import os

sys.path.append(os.path.abspath("src"))

from WebSocket.websocket_server import start_websocket_server
from Rover.rover import Rover

def lancer_websocket():
    print("🔧 Démarrage du serveur WebSocket...")
    asyncio.run(start_websocket_server())

def main():
    # Lancer le WebSocket dans un thread indépendant
    websocket_thread = threading.Thread(target=lancer_websocket, daemon=True)
    websocket_thread.start()

    planete = (10, 10)
    obstacles = [(3, 3), (5, 5), (7, 7)]
    rover = Rover(5, 5, 'N', planete, obstacles)

    print("🚀 Bienvenue sur Mars ! Vous êtes au contrôle du Rover.")
    print("Commandes : A = avancer | R = reculer | G = gauche | D = droite | S = séquence | Q = quitter")

    while True:
        try:
            commande = input("Commande : ").strip().upper()

            if commande == 'Q':
                print("👋 Fin de mission. Au revoir depuis Mars !")
                break
            elif commande == 'S':
                sequence = input("Séquence de commandes : ").strip().upper()
                rover.executer_commandes(sequence)
            elif commande in ['A', 'R']:
                rover.deplacer(commande)
            elif commande in ['G', 'D']:
                rover.tourner(commande)
            else:
                print("❌ Commande invalide.")
                continue

            print("📍 Position actuelle :", rover.get_position())
            rover.afficher_carte()

        except KeyboardInterrupt:
            print("\n🔌 Interruption manuelle. Arrêt du rover.")
            break

if __name__ == "__main__":
    main()
