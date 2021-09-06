# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
关于websocket的尝试
pip install websocket
'''

import time
import uuid
import asyncio
import websockets


def server_and_client():
    async def server(websocket, path):
        while True:
            recv_text = await websocket.recv()
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            echo = f"Server got message: [{recv_text}] at {t}"
            await websocket.send(echo)

    async def client(uri, name):
        # 暂停1秒，确保server已经启动
        time.sleep(1)
        async with websockets.connect(uri) as websocket:
            await websocket.send(f"{name} connect server")
            count = 1
            while True:
                message = str(uuid.uuid4())
                await websocket.send(f"{name} with {message}")
                recv_text = await websocket.recv()
                time.sleep(1)
                print(f"> {recv_text}")
                if count >= 5000:
                    await websocket.close(reason="user exit")
                    break
                count += 1

    async def main():
        start_server = websockets.serve(server, 'localhost', 40001)
        await asyncio.gather(
            start_server,
            # client("ws://localhost:40001", "C01"),
            # client("ws://localhost:40001", "C02")
        )

    asyncio.run(main())


if __name__ == '__main__':
    server_and_client()
