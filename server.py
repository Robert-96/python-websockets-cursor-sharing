#!/usr/bin/env python

import asyncio
import http
import json
import os
import random
import signal
import uuid

import websockets

CONNECTIONS = set()


async def handle_client(websocket, path):
    id = str(uuid.uuid4())
    color = random.randint(0, 360)

    CONNECTIONS.add(websocket)

    try:
        async for message in websocket:
            print(f"<<< {message}")

            payload = json.loads(message)
            payload["sender"] = id
            payload["color"] = color

            outbound = json.dumps(payload)
            print(f">>> {outbound}")

            websockets.broadcast(CONNECTIONS, outbound)
    finally:
        CONNECTIONS.remove(websocket)


async def health_check(path, request_headers):
    if path == "/healthz":
        return http.HTTPStatus.OK, [], b"OK\n"


async def main():
    host = os.environ.get("WS_HOST", "127.0.0.1").strip()
    port = int(os.environ.get("WS_PORT", "7171"))

    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    async with websockets.serve(handle_client, host, port, process_request=health_check):
        await stop


if __name__ == "__main__":
    asyncio.run(main())
