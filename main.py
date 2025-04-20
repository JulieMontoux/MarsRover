import asyncio
import threading
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
                
from WebSocket.websocket_server import start_websocket_server
from MissionControl.missionControl import MissionControl

def lancer_websocket():
    print("🔧 Démarrage du serveur WebSocket...")
    asyncio.run(start_websocket_server())

def main():
    # Lancer le serveur WebSocket dans un thread parallèle
    websocket_thread = threading.Thread(target=lancer_websocket, daemon=True)
    websocket_thread.start()

    # Initialisation de la mission (Rover + Planète + Obstacles)
    planete = (10, 10)
    obstacles = [(3, 3), (5, 5), (7, 7)]
    mission = MissionControl(planete, obstacles)

    print("🚀 Bienvenue sur Mars ! Vous êtes au contrôle du Rover.")
    print("Commandes : A = avancer | R = reculer | G = gauche | D = droite | POSITION = état actuel | Q = quitter")

    while True:
        try:
            commande = input("Commande : ").strip().upper()

            if commande == 'Q':
                print("👋 Fin de mission. Au revoir depuis Mars !")
                break
            elif commande == "POSITION":
                print("📍 Position actuelle :", mission.get_position())
            elif commande in ['A', 'R', 'G', 'D']:
                mission.executer_commande(commande)
                print("📍 Nouvelle position :", mission.get_position())
                mission.afficher_carte()
            else:
                print("❌ Commande invalide. Essayez A, R, G, D, POSITION ou Q.")

        except KeyboardInterrupt:
            print("\n🔌 Interruption manuelle. Arrêt du rover.")
            break

if __name__ == "__main__":
    main()
