# 信号量是进程同步过程中一个比较重要的角色。它可以控制临界资源的数量，实现多个进程同时访问共享资源，限制进程的并发量
#  用 multiprocessing 库中的 Semaphore 来实现信号量

# 多个进程共享资源，同时又限制同时可访问的进程数量

# 生产者和消费者问题
from multiprocessing import Process, Semaphore, Lock, Queue
import time

buffer = Queue(10)  # 定义一个共享队列
empty = Semaphore(2)  # 定义一个信号量，表示缓冲区空余数
full = Semaphore(0)   # 定义一个信号量，表示缓冲区占用数
lock = Lock()

class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()  #
            lock.acquire()
            buffer.get()
            print('Consumer pop an element')
            time.sleep(1)
            lock.release()
            empty.release()

class Producer(Process):  # 生产者进程
    def run(self):
        global buffer, empty, full, lock
        while True:
            empty.acquire()  # 占用一个缓冲区位置，缓冲区空闲区大小减 1
            lock.acquire() # 接下来进行加锁，
            buffer.put(1)  # 对缓冲区进行操作
            print('Producer append an element')
            time.sleep(1)
            lock.release() # 释放锁，最后让代表占用的缓冲区位置数量加 1
            full.release()

if __name__ == '__main__':

    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')
