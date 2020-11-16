import threading
import time

count = 0

# class MyThread(threading.Thread):
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         global count
#         temp = count + 1
#         time.sleep(0.001)
#         count = temp
#
# threads = []
#
# for _ in range(1000):
#     thread = MyThread()
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# print(f'Final count: {count}')  # count应该是1000，但是最终输出的结果是54

# 因为 count 这个值是共享的，每个线程都可以在执行 temp = count 这行代码时拿到当前 count 的值，
# 但是这些线程中的一些线程可能是并发或者并行执行的，这就导致不同的线程拿到的可能是同一个 count 值，
# 最后导致有些线程的 count 的加 1 操作并没有生效，导致最后的结果偏小

# 所以，如果多个线程同时对某个数据进行读取或修改，就会出现不可预料的结果。
# 为了避免这种情况，我们需要对多个线程进行同步，要实现同步，我们可以对需要操作的数据进行加锁保护，这里就需要用到 threading.Lock

# 加锁保护是什么意思呢？
# 就是说，某个线程在对数据进行操作前，需要先加锁，这样其他的线程发现被加锁了之后，就无法继续向下执行，会一直等待锁被释放，
# 只有加锁的线程把锁释放了，其他的线程才能继续加锁并对数据做修改，修改完了再释放锁。
# 这样可以确保同一时间只有一个线程操作数据，多个线程不会再同时读取和修改同一个数据，这样最后的运行结果就是对的了。

# 修改

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global count
        lock.acquire()  # 获取前加锁
        temp = count + 1
        time.sleep(0.001)
        count = temp
        lock.release() # 修改完之后释放

lock = threading.Lock() # 声明一个lock对象
threads = []
for _ in range(1000):
    thread = MyThread()
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(f'Final count: {count}')
