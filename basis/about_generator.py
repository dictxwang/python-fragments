# -*- coding: utf8 -*-
__author__ = 'wangqiang'

'''
生成器generator，yield相关的应用
'''
import time
import random


def producer_consumer():
    def consumer():
        resp = ""
        while True:
            req = yield resp
            time.sleep(1)
            # if not req:
            #     continue
            print("[Consumer] consuming {} ...".format(req))
            resp = "200 OK"

    def producer(consumer):
        # 通过send方法开启一个generator
        consumer.send(None)
        for n in range(1, 3):
            time.sleep(1)
            print("[Producer] producing {} ...".format(n))
            resp = consumer.send(n)
            print("[Producer] consumer return :{}".format(resp))
        consumer.close()

    c = consumer()
    producer(c)


def list_or_generator():
    # 列表
    l = [x * x for x in range(10)]
    print(l)

    # 生成器
    g = (x * x for x in range(10))
    for v in g:
        print(v)


def generator_next():

    def cf():
        while True:
            val = yield
            print("cf consuming {}".format(val))

    def pf(c):
        while True:
            n = random.randint(1, 10)
            c.send(n)
            yield

    c = cf()
    # 调用send方法开启generator
    c.send(None)
    p = pf(c)

    for n in range(1, 10):
        next(p)


def generator_yield_from():

    def cf(names):
        for name in names:
            # 这里yield好比async
            yield "hello " + name

    def main():
        # 这里yield from好比await
        yield from cf(["liudehua", "张学友"])

    m = main()
    for welcome in m:
        print(welcome)
    # print(next(m)) # 迭代器已经空，这里会报错：StopIteration


def generator_yield_from_02():

    def main():
        # 返回一个generator
        yield from (x * x for x in range(10))

    m = main()
    for xsqrt in m:
        print(xsqrt)


if __name__ == "__main__":
    # producer_consumer()
    # list_or_generator()
    # generator_next()
    # generator_yield_from()
    generator_yield_from_02()
