"""
threading.Thread(target=XX).start()
threading.enumerate() 线程数量
主线程会等待所有的子线程结束后才结束
定义一个新的子类class，只要继承threading.Thread就可以了，然后重写run方法

互斥锁：创建锁mutex = threading.Lock()；锁定mutex.acquire()；释放mutex.release()

multiprocessing.Process(target=XX).start() 子进程
os.getpid()获取当前进程的进程号
is_alive()：判断进程子进程是否还在活着
join([timeout])：等待子进程执行结束，或等待多少秒
terminate()：不管任务是否完成，立即终止子进程

multiprocessing.Queue(N).qsize()/empty()/full()/get_nowait()/get([block[, timeout]])/put(item,[block[, timeout]])
使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()

multiprocessing.Pool(N).terminate()/close()/join()/apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程）


"""

import threading
from multiprocessing import Process
import os
from time import sleep

g_num = 0
# 创建一个互斥锁
# 默认是未上锁的状态
mutex = threading.Lock()

def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print("---test1---g_num=%d"%g_num)

def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print("---test2---g_num=%d"%g_num)

def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)


if __name__ == '__main__':
    # 创建2个线程，让他们各自对g_num加1000000次
    p1 = threading.Thread(target=test1, args=(1000000,))
    p1.start()

    p2 = threading.Thread(target=test2, args=(1000000,))
    p2.start()

    # 等待计算完成
    while len(threading.enumerate()) != 1:
        sleep(1)

    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)

    p = Process(target=run_proc, args=('test', 18), kwargs={"m": 20})
    p.start()
    sleep(1)  # 1秒中之后，立即结束子进程
    p.terminate()
    p.join()