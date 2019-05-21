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

 L = [ x*2 for x in range(5)]   --->   G = ( x*2 for x in range(5))    列表生成式[]--->生成器()
 将原本在迭代器__next__方法中实现的基本逻辑放到一个函数中来实现，但是将每次迭代返回数值的return换成了yield，此时新定义的函数便不再是函数，而是一个生成器了。
 简单来说：只要在def中有yield关键字的 就称为 生成器
 yield关键字有两点作用：
    保存当前运行状态（断点），然后暂停执行，即将生成器（函数）挂起
    将yield关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用
可以使用next()函数让生成器从断点处继续执行，即唤醒生成器（函数）,还可以使用send()函数来唤醒执行(传入附加参数);Python3中的生成器可以使用return返回最终运行的返回值
gevent自动实现协程，是yield的进化版，greenlet可以手动控制

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