# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
多进程方式的生成者-消费者模型
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
            mq.put((mt[0], uuid.uuid1()), block=True, timeout=0.01)
        except Exception as exp:
            pass
        # 模拟数据通信的延时
        time.sleep(random.randint(0, 2))


def consumer(name, mq):
    '''
    消费者，从队列中取出数据，并实现业务逻辑
    :param name: 消费者名称
    :param mq: 共享队列
    :return:
    '''
    while True:
        # 用于task的去重
        task_map = {}
        get_times = 0
        try:
            if not mq.empty():
                task = mq.get(block=True, timeout=0)
                if task:
                    # 更新task，同类型task只保存最新的一个
                    task_map[task[0]] = task[1]
        except Exception as exp:
            break
        get_times += 1
        if get_times >= 10:
            break
        # 执行task，此处用输出task信息模拟
        for mt, msg in task_map.items():
            print("{} consume {}-{}".format(name, mt, msg))

        time.sleep(random.randint(0, 2))


if __name__ == "__main__":

    message_queue = Queue(maxsize=1000)
    # 构建消费者
    for i in range(3):
        c = threading.Thread(target=consumer, args=("c{}".format(i), message_queue))
        c.start()
        print("consumer-{} started".format(i))

    # 构建生产者
    p1 = threading.Thread(target=producer, args=("01", message_queue))
    p1.start()
    print("producer started")
