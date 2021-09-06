# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
基于asyncio的生产者消费者模型
'''

import asyncio
import random
import uuid


async def producer(name, aq):
    singnal = 1
    while True:
        await asyncio.sleep(0.1)
        await aq.put(f"{name} put {singnal} - {uuid.uuid1()}")
        singnal += 1


async def consumer(name, aq):
    while True:
        m = await aq.get()
        print(f"[consumer-{name}] consume {m}")
        # asyncio.sleep会让出cpu控制权
        await asyncio.sleep(random.randint(50, 500) * 0.001)


async def main(name):
    aq = asyncio.queues.Queue()
    # 通过gather模式，任务将不会被取消（即使子任务不带循环，也不会退出）
    # 但是gather模式，多个子任务可以并行
    await asyncio.gather(
        producer(name, aq),
        consumer("c001", aq),
        consumer("c002", aq)
    )


if __name__ == '__main__':
    asyncio.run(main("p001"))
    # 两种方式是等价的，asyncio.run属于3.7+版本的api
    # asyncio.get_event_loop().run_until_complete(main("p001"))
