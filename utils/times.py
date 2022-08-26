import time
import datetime


def timestamp():
    """时间戳"""
    return time.time()


def dt_strftime(fmt):
    """格式化时间"""
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds):
    """睡眠时间"""
    time.sleep(seconds)


if __name__ == '__main__':
    print(timestamp())
    print(dt_strftime("%Y%m%d%H%M%S"))
