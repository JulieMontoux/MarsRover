import asyncio
import websockets

async def test():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            cmd = input("Commande (A/R/G/D/Séquence ou POSITION) : ").upper()
            await websocket.send(cmd)
            response = await websocket.recv()
            print(f"Rover dit : {response}")

asyncio.run(test())
