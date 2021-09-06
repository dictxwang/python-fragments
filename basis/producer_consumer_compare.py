# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import queue
import threading
import time
import asyncio


def original_producer_consumer(tcount):

    def producer(q, tcount):
        for i in range(0, tcount):
            q.put(i)

    def consumer(q, tcount):
        st = time.time()
        for i in range(0, tcount):
            msg = q.get()
            print(f"consume {msg}")
        cost = time.time() - st
        print(f"orignial total cost {cost} seconds")

    q = queue.Queue()
    tp = threading.Thread(target=producer, args=(q, tcount))
    tc = threading.Thread(target=consumer, args=(q, tcount))
    tp.start()
    tc.start()


def asyncio_producer_consumer(tcount):

    async def producer(aq, tcount):
        for i in range(0, tcount):
            await aq.put(i)

    async def consumer(aq, tcount):
        st = time.time()
        for i in range(0, tcount):
            msg = await aq.get()
            print(f"consume {msg}")
        cost = time.time() - st
        print(f"asyncio total cost {cost} seconds")

    async def main():
        aq = asyncio.queues.Queue()
        await asyncio.gather(
            producer(aq, tcount),
            consumer(aq, tcount)
        )

    asyncio.run(main())


if __name__ == '__main__':
    tcount = 100000
    original_producer_consumer(tcount)
    # asyncio_producer_consumer(tcount)
