# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
基于多线程实现1对多的websocket
一个server，多个client
'''

import websockets
import threading
import asyncio
import time
import uuid
import random


def start_server(host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(websockets.serve(server, host, port))
    # 如果没有run_forever，server会立即退出
    loop.run_forever()


def start_server_thread(host, port):
    t = threading.Thread(target=start_server, args=(host, port))
    t.start()
    print(f"Serve ready at {host}:{port}")
    return t


async def server(websocket, path):
    while True:
        try:
            recv_text = await websocket.recv()
            t = time.strftime("%Y-%m-%d %H:%M%S", time.localtime())
            echo = f"Server got message: {recv_text} at {t}"
            await websocket.send(echo)
        except Exception as exp:
            if exp.code == 1000:
                print(f"connection close with {exp.code} for reason {exp.reason}")
            break


async def client(uri, name):
    # 暂停一秒，确保端口已经启动
    time.sleep(1)
    async with websockets.connect(uri) as websocket:
        await websocket.send(f"{name} connect server")
        for i in range(5):
            message = str(uuid.uuid4())
            await websocket.send(f"{name} send {message}")
            recv_text = await websocket.recv()
            print(f">{recv_text}")
            time.sleep(random.randint(1, 3))
        await websocket.close(reason=f"{name} close connection")


def start_client(uri, name):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(client(uri, name))


def start_client_threads(uri, count):
    threads = [threading.Thread(target=start_client, args=(uri, f"Client-{i}")) for i in range(count)]
    [t.start() for t in threads]
    [t.join() for t in threads]


def start_client_threads_delay(uri, count, delay):
    time.sleep(delay)
    threads = [threading.Thread(target=start_client, args=(uri, f"DelayClient-{i}")) for i in range(count)]
    [t.start() for t in threads]
    [t.join() for t in threads]


if __name__ == '__main__':
    # 启动websocket服务端
    t_server = start_server_thread("localhost", "40002")
    start_client_threads("ws://localhost:40002", 10)
    # 模拟中途连接websocket
    start_client_threads_delay("ws://localhost:40002", 5, 10)
    t_server.join()
