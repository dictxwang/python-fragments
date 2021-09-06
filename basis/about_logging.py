# -*- coding: utf8 -*-
__author__ = 'wangqiang'

import threading
import logging
from logging.handlers import TimedRotatingFileHandler
import os


class LoggerFactory(object):
    _logger_instance_map = {}
    _create_instance_lock = threading.Lock()

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    def get_logger(cls, logger_name, level="INFO", path="data/logs") -> logging:
        """
        获取logger对象的静态方法
        :param logger_name: 日志文件名
        :param level: 日志级别
        :param path: 日志文件存放目录
        :return:
        """
        if logger_name not in cls._logger_instance_map:
            with cls._create_instance_lock:
                if logger_name not in cls._logger_instance_map:
                    if not os.path.exists(path):
                        os.mkdir(path)
                    logger = logging.getLogger(name=logger_name)
                    log_formatter = logging.Formatter("%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
                    file_name = os.path.join(path, logger_name + ".log")
                    # 输出到文件
                    file_handler = TimedRotatingFileHandler(filename=file_name, when="midnight", backupCount=3)
                    file_handler.suffix = "%Y-%m-%d"
                    file_handler.setFormatter(log_formatter)
                    file_handler.setLevel(level=level)
                    logger.addHandler(file_handler)
                    # 输出到控制台
                    stream_handler = logging.StreamHandler()
                    stream_handler.setFormatter(log_formatter)
                    stream_handler.setLevel(level=level)
                    logger.addHandler(stream_handler)
                    logger.setLevel(level=level)
                    cls._logger_instance_map[logger_name] = logger
        return cls._logger_instance_map[logger_name]


if __name__ == "__main__":
    logger = LoggerFactory.get_logger("log_001", level="INFO")
    logger.info("a line log content.")
