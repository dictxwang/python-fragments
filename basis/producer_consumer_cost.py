# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
多进程方式的生成者-消费者模型（测试耗时）
多线程的实现
'''

import threading
from queue import Queue
import time
import uuid
import random


def producer(name, mq):
    '''
    生产者，向队列插入数据
    :param mq: 共享队列
    :return:
    '''
    while True:
        # 元组的第一项用于表示消息类型，元组第二项使用uuid模拟消息内容
        mt = ['a', 'b', 'c']
        random.shuffle(mt)
        try:
            mq.put((mt[0], int(time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID) * 1000000), uuid.uuid1()), block=True, timeout=0.01)
        except Exception as exp:
            pass
        # 模拟数据通信的延时
        rnd = random.randint(0, 10)
        if rnd >= 0:
            time.sleep(rnd * 0.001)


def consumer(name, mq):
    '''
    消费者，从队列中取出数据，并实现业务逻辑
    :param name: 消费者名称
    :param mq: 共享队列
    :return:
    '''
    tcount = 0
    ocount = 0
    ccount = 0
    while True:
        try:
            task = mq.get()
            now = int(time.clock_gettime(time.CLOCK_PROCESS_CPUTIME_ID) * 1000000)
            tcount += 1
            if task:
                time_diff = now - task[1]
                ccount += time_diff
                # print("[{}] get message time_diff:{}μs".format(name, time_diff))
                time_diff_limit = 800
                if time_diff > time_diff_limit:
                    ocount += 1
                    print("[{}] get message time_diff {}μs > {}μs".format(name, time_diff, time_diff_limit))
                    print("timeout-count={},total-count={}, avg-time-diff={}μs".format(ocount, tcount, ccount // tcount))
        except Exception as exp:
            break
        finally:
            time.sleep(0.001)


if __name__ == "_+_main__":

    message_queue = Queue(maxsize=1000)
    # 构建消费者
    for i in range(4):
        c = threading.Thread(target=consumer, args=("c{}".format(i), message_queue))
        c.start()
        print("consumer-{} started".format(i))

    # 构建生产者
    p1 = threading.Thread(target=producer, args=("01", message_queue))
    p1.start()
    print("producer started")


if __name__ == "__main__":
    print(1)


if __name__ == "__main__":
    print(2)
