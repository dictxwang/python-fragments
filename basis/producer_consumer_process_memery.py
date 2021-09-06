# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
基于内存共享的生产者消费者模型
'''

import time
import uuid
from multiprocessing import Process
from multiprocessing import Manager


def producer(name, q):

    while True:
        msg = uuid.uuid1()
        q.put(msg)
        print("producer-{} put message {}".format(name, msg))
        time.sleep(0.1)


def consumer(name, q):

    while True:
        msg = q.get()
        print("consumer-{} get message {}".format(name, msg))


if __name__ == "__main__":

    manager = Manager()
    q = manager.Queue(maxsize=100)
    p1 = Process(target=producer, args=("p001", q))
    p1.start()

    c1 = Process(target=consumer, args=("c01", q))
    c2 = Process(target=consumer, args=("c02", q))
    c1.start()
    c2.start()

    # 这里需要执行join，否则manager会直接退出
    # 另外join的含义是等待子进程结束，所以一定要在所有子进程start之后再进行join
    p1.join()
    c1.join()
    c2.join()
