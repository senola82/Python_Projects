import asyncio
import websockets

connected_clients = set()

async def echo(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print(f"Received: {message}")
            await websocket.send(f"echo: {message}")
    finally:
        connected_clients.remove(websocket)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    server = websockets.serve(echo, "0.0.0.0", 8765)
    loop.run_until_complete(server)
    print("WebSocket server started on ws://0.0.0.0:8765")
    loop.run_forever()
