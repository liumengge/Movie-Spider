import threading
import time

def target(second):
    print(f'Threading {threading.current_thread().name} is running')  # 打印当前线程的名字
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)  # 休眠second秒
    print(f'Threading {threading.current_thread().name} is ended')

# print(f'Threading {threading.current_thread().name} is running')

# for i in [1, 5]:
#     thread = threading.Thread(target=target, args=[i])  # 通过 Thead 类新建了两个线程，target 参数就是我们定义的方法名，args 以列表的形式传递，两次循环中，这里 i 分别就是 1 和 5，这样两个线程就分别休眠 1 秒和 5 秒
#     thread.start()  # 声明完成之后，我们调用 start 方法即可开始线程的运行

# print(f'Threading {threading.current_thread().name} is ended')


# Threading MainThread is running
# Threading Thread-1 is running
# Threading Thread-1 sleep 1s
# Threading Thread-2 is running
# Threading Thread-2 sleep 5s
# Threading MainThread is ended
#
# Threading Thread-1 is ended
# Threading Thread-2 is ended

# 这里一共产生了三个线程，分别是主线程 MainThread 和两个子线程 Thread-1、Thread-2。
# 另外我们观察到，主线程首先运行结束，紧接着 Thread-1、Thread-2 才接连运行结束，分别间隔了 1 秒和 4 秒。
# 这说明主线程并没有等待子线程运行完毕才结束运行，而是直接退出了，有点不符合常理

# 如果我们想要主线程等待子线程运行完毕之后才退出，可以让每个子线程对象都调用下 join 方法

print(f'Threading {threading.current_thread().name} is running')
threads = []
for i in [1, 5]:
    thread = threading.Thread(target=target, args=[i])
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')

# Threading MainThread is running
# Threading Thread-1 is running
# Threading Thread-1 sleep 1s
# Threading Thread-2 is running
# Threading Thread-2 sleep 5s
# Threading Thread-1 is ended
# Threading Thread-2 is ended
# Threading MainThread is ended



# 继承 Thread 类创建子线程

class MyThread(threading.Thread):

    def __init__(self, second):
        threading.Thread.__init__(self)
        self.second = second

    def run(self):
        print(f'Threading {threading.current_thread().name} is running')
        print(f'Threading {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Threading {threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is running')

threads = []
for i in [1, 5]:
    thread = MyThread(i)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f'Threading {threading.current_thread().name} is ended')