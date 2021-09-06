# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import pickle


class World:

    version = "0.1"

    def __init__(self, name="xxx"):
        self._name = name

    def sayHello(self):
        print("hello, this is world of {}.".format(self._name))

    @classmethod
    def getVersion(cls):
        return cls.version


if __name__ == "__main__":

    world = World("python")
    world.sayHello()
    print(World.getVersion())

    world_bytes = pickle.dumps(world)
    with open("data/pickle_001.obj", mode="wb") as fp:
        fp.write(world_bytes)
        fp.flush()

    saved_bytes = None
    with open("data/pickle_001.obj", mode="rb") as fp:
        saved_bytes = fp.read()
    saved_world = pickle.loads(saved_bytes)
    saved_world.sayHello()

    saved_world = pickle.load(open("data/pickle_001.obj", mode="rb"), encoding="utf8")
    saved_world.sayHello()
