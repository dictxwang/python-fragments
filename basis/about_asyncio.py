# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import asyncio
import functools
import asyncio.queues as queues
import time
import datetime
import uuid

'''
require python3.8+
'''


def async_await_01():
    async def say_after(delay, what):
        await asyncio.sleep(delay)
        print(what)

    async def main():
        print("started")
        st = time.time()
        await say_after(1, "hello")
        await say_after(2, "world")
        print("runtime: ", time.time() - st)
        print("finished")

    # from python3.7 use asyncio.run()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


def async_await_02():
    async def say_after(delay, what):
        # 这里的sleep不会造成整个事件循环中断
        # asyncio.sleep()实际上是在内部实现了一个future对象
        await asyncio.sleep(delay)
        print(what)

    async def main():
        print("started")
        # from python3.7 use create_task()
        t1 = asyncio.create_task(say_after(1, "hello"))
        t2 = asyncio.ensure_future(say_after(2, "world"))
        st = time.time()
        # 两个任务将并行执行
        await t1
        await t2
        print("runtime: ", time.time() - st)
        print("finished")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


def async_await_03():
    async def say_after(delay, what):
        # 这里的sleep会造成事件循环中断
        await sleep(delay)
        print(what)

    async def sleep(delay):
        time.sleep(delay)

    async def main():
        print("started")
        t1 = asyncio.ensure_future(say_after(1, "hello"))
        t2 = asyncio.ensure_future(say_after(2, "world"))
        st = time.time()
        await t1
        await t2
        print("runtime: ", time.time() - st)
        print("finished")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


def async_await_04():
    async def say_hello(delay, name):
        await asyncio.sleep(delay)
        print("welcome {}".format(name))

    def main():
        print("started")
        st = time.time()
        loop = asyncio.get_event_loop()
        tasks = [
            asyncio.ensure_future(say_hello(1, "liudehua")),
            asyncio.ensure_future(say_hello(3, "liming")),
            asyncio.ensure_future(say_hello(4, "zhangxueyou")),
            asyncio.ensure_future(say_hello(2, "guofucheng"))
        ]
        loop.run_until_complete(asyncio.wait(tasks))
        print("runtime: {}".format(time.time() - st))
        print("finished")

    main()


def async_await_gather():
    async def factorial(name, number):
        f = 1
        for i in range(2, number + 1):
            print(f"Task {name}: Compute factorial ({i})...")
            await asyncio.sleep(1)
            f *= i
        print(f"Task {name}: factorial({number})={f}")

    async def main():
        # 这里的任务将并发进行
        await asyncio.gather(
            factorial("A", 2),
            factorial("B", 3),
            factorial("C", 4)
        )
    asyncio.run(main())


def async_await_wait_for():
    async def eternity():
        await asyncio.sleep(1000)
        print("yay")

    async def main():
        try:
            await asyncio.wait_for(eternity(), timeout=1.0)
        except asyncio.TimeoutError:
            print("timeout")
    asyncio.run(main())


def running_loop():
    async def display_date():
        loop = asyncio.get_running_loop()
        end_time = loop.time() + 5.0
        while True:
            print(datetime.datetime.now())
            if (loop.time() + 1.0) >= end_time:
                break
            await asyncio.sleep(1)
    asyncio.run(display_date())


def async_await_blocking_io():
    def blocking_io():
        print(f"start blocking_io at {time.strftime('%X')}")
        time.sleep(1)
        print(f"blocking_io complete at {time.strftime('%X')}")

    async def main():
        await asyncio.gather(
            asyncio.to_thread(blocking_io),
            asyncio.sleep(3)
        )
        print(f"finished main at {time.strftime('%X')}")

    asyncio.run(main())


def asyncio_producer_consumer():
    '''
    利用asyncio创建的生产者消费者模型
    :return:
    '''
    async def producer(q):
        while True:
            await asyncio.sleep(0.001)
            await q.put(uuid.uuid1())

    async def consumer(q):
        while True:
            # await asyncio.sleep(0.2)
            m = await q.get()
            print(m)

    async def main():
        q = queues.Queue()
        await asyncio.gather(
            producer(q),
            consumer(q)
        )

    asyncio.run(main())


def asyncio_task_callback():
    '''
    给task添加回调方法
    :return: 如果没有返回值，callback中的future.result()将返回None
    '''
    async def say_hi(delay, name):
        await asyncio.sleep(delay)
        print(f"welcome {name}")
        return name.upper()

    def callback(future):
        print("callback method running")
        print(f"future.result() in callback is {future.result()}")

    async def main():
        task = asyncio.create_task(say_hi(1, "wangqiang"))
        task.add_done_callback(callback)
        await task
        print(f"task result():{task.result()}")
    asyncio.run(main())


def asyncio_future_result():
    '''
    包含future的结果
    :return:
    '''
    async def multi(future, first, second):
        await asyncio.sleep(1)
        future.set_result(str(first * second))

    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(multi(future, 10, 20))
    loop.run_until_complete(future)
    print(f"future result: {future.result()}")
    loop.close()


def asyncio_future_result_02():
    '''
    future result的使用
    :return:
    '''
    async def add(future, fist, second):
        await asyncio.sleep(1)
        future.set_result(fist + second)

    future = asyncio.Future()
    asyncio.run(add(future, 1, 3))
    print(f"future result: {future.result()}")


if __name__ == "__main__":
    async_await_01()
    async_await_02()
    async_await_03()
    async_await_04()
    async_await_gather()
    async_await_wait_for()
    running_loop()
    async_await_blocking_io()
    asyncio_producer_consumer()
    asyncio_task_callback()
    asyncio_future_result()
    asyncio_future_result_02()
