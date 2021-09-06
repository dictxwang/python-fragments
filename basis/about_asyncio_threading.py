# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
asyncio与threading多线程的应用
'''

import asyncio
import threading
import random


def thr(i):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(do_stuff(i))
    loop.close()


async def do_stuff(i):
    await asyncio.sleep(random.uniform(0.1, 0.5))
    print(i)


def main():
    num_threads = 10
    threads = [threading.Thread(target=thr, args=(i,)) for i in range(num_threads)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    print("bye")


if __name__ == '__main__':
    main()
