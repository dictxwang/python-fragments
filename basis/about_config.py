# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import configparser

if __name__ == "__main__":

    conf = configparser.ConfigParser()
    conf.read("data/config_001.properties")
    print(conf.get("core", "profile"))
    print(conf.get("mysql", "db"))
    # 获取bool类型配置
    print(conf.getboolean("types", "open"))
    # 获取整型配置
    print(conf.getint("types", "times"))
