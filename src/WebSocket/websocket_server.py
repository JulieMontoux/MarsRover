import asyncio
import websockets
from Rover.rover import Rover

planete = (10, 10)
obstacles = [(3, 3), (5, 5), (7, 7)]
rover = Rover(0, 0, 'N', planete, obstacles)

async def handle_connection(websocket):
    print("📡 Nouveau client connecté !")
    await websocket.send("Connexion établie avec le rover.")

    async for message in websocket:
        message = message.strip().upper()
        print(f"🎮 Commande reçue via WebSocket : {message}")

        if message == "POSITION":
            await websocket.send(rover.get_position())
        elif set(message).issubset({'A', 'R', 'G', 'D'}):
            rover.executer_commandes(message)
            await websocket.send(rover.get_position())
            rover.afficher_carte()  # ✅ affiche la carte dans le terminal serveur
        else:
            await websocket.send(f"Commande invalide : {message}")


async def start_websocket_server():
    print("🔌 WebSocket en écoute sur ws://localhost:8765")
    async with websockets.serve(handle_connection, "localhost", 8765):
        await asyncio.Future()
