import threading
import time


def coding():
    for x in range(3):
        print("%s正在写代码" %threading.current_thread())
        time.sleep(1)


def drawing():
    for x in range(3):
        print("%s正在画图" %threading.current_thread())
        time.sleep(1)


def multi_thread():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()

    print(threading.enumerate())

if __name__ == '__main__':
    multi_thread()