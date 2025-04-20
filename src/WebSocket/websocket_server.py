import asyncio
import websockets
from Rover.rover import Rover
from Communication.protocole import ProtocoleCommunication

planete = (10, 10)
obstacles = [(3, 3), (5, 5), (7, 7)]
rover = Rover(0, 0, 'N', planete, obstacles)

async def handle_connection(websocket):
    print("📡 Nouveau client connecté !")
    await websocket.send("Connexion établie avec le rover.")

    async for message in websocket:
        type_commande, contenu = ProtocoleCommunication.parser_message(message)

        if type_commande == "position":
            position = rover.get_position()
            await websocket.send(ProtocoleCommunication.formater_reponse(position))

        elif type_commande == "mouvement":
            rover.executer_commandes(contenu)
            position = rover.get_position()
            await websocket.send(ProtocoleCommunication.formater_reponse(position))
            rover.afficher_carte()

        else:
            await websocket.send("❌ Commande invalide. Essayez : A, R, G, D, ou POSITION.")


async def start_websocket_server():
    print("🔌 WebSocket en écoute sur ws://localhost:8765")
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()
