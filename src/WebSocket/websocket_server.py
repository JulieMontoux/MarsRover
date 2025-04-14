import asyncio
import websockets
import json
from Rover.rover import Rover

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

planete = (10, 10)
obstacles = [(3, 3), (5, 5), (7, 7)]
rover = Rover(0, 0, 'N', planete, obstacles)

async def handle_connection(websocket):
    await websocket.send("Connexion établie avec le rover.")
    async for message in websocket:
        print(f"Commande reçue : {message}")
        try:
            message = message.strip().upper()
            if message == "POSITION":
                await websocket.send(rover.get_position())
            elif set(message).issubset({'A', 'R', 'G', 'D'}):
                rover.executer_commandes(message)
                await websocket.send(rover.get_position())
            else:
                await websocket.send(f"Commande invalide : {message}")
        except Exception as e:
            await websocket.send(f"Erreur : {str(e)}")

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Serveur WebSocket en écoute sur ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
