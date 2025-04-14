import asyncio
import websockets

async def test():
    uri = "ws://localhost:8765"
    print("🌐 Tentative de connexion au serveur WebSocket...")
    async with websockets.connect(uri) as websocket:
        print("✅ Connecté au serveur WebSocket !")
        while True:
            cmd = input("Commande (A/R/G/D ou POSITION) : ").upper()
            await websocket.send(cmd)
            response = await websocket.recv()
            print(f"📡 Réponse du rover : {response}")

asyncio.run(test())
