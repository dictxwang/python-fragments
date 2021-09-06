# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
多进程方式的生成者-消费者模型
多进程的实现，借助外部存储（如redis）实现数据共享

pip install redis
'''

import redis
import multiprocessing
import time
import uuid
import random


def producer(name, share_cache, cache_key):
    '''
    生产者，执行业务逻辑，并向共享缓存写入消息
    :param name: 生产者名字代号
    :param share_cache: 共享缓存（redis——client）
    :param cache_key: 共享缓存队列key
    :return:
    '''
    while True:
        if share_cache.llen(cache_key) > 10000:
            time.sleep(random.randint(0, 1))
            break
        # 元组的第一项用于表示消息类型，元组第二项使用uuid模拟消息内容
        mt = ['a', 'b', 'c']
        random.shuffle(mt)
        try:
            #todo 补充业务逻辑
            msg = "{}#{}".format(mt[0], uuid.uuid1())
            # 生产消息
            share_cache.lpush(cache_key, msg)
            print("{} produce {}".format(name, msg))
        except Exception as exp:
            pass
        # 模拟数据通信的延时
        time.sleep(random.randint(0, 1))


def consumer(name, share_cache, cache_key):
    '''
    消费者，从共享缓存中获取消息，并执行业务逻辑
    :param name: 消费者名字代号
    :param share_cache: 共享缓存（redis——client）
    :param cache_key: 共享缓存队列key
    :return:
    '''
    while True:
        # 用于task的去重
        task_map = {}
        get_times = 0
        try:
            if share_cache.llen(cache_key) > 0:
                task = share_cache.rpop(cache_key)
                if task:
                    task = task.decode()
                    # 更新task，同类型task只保存最新的一个
                    parts = task.split("#")
                    task_map[parts[0]] = parts[1]
        except Exception as exp:
            break
        get_times += 1
        if get_times >= 10:
            break
        # 执行task，此处用输出task信息模拟
        if len(task_map) > 0:
            for mt, msg in task_map.items():
                # todo 用print代替正常的业务逻辑
                print("{} consume {}-{}".format(name, mt, msg))
        else:
            time.sleep(random.randint(0, 1))


if __name__ == "__main__":

    redis_share = redis.Redis(host='127.0.0.1', port=6666, db=15, password="")
    cache_key = "price_message"
    # 构建多个消费者
    for i in range(3):
        c = multiprocessing.Process(target=consumer, args=("c{}".format(i), redis_share, cache_key))
        c.start()
        print("consumer-{} started".format(i))

    # 构建多个生产者
    p1 = multiprocessing.Process(target=producer, args=("p01", redis_share, cache_key))
    p1.start()
    p2 = multiprocessing.Process(target=producer, args=("p02", redis_share, cache_key))
    p2.start()
    print("producer started")