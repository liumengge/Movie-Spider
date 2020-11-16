
# 如果一个线程被设置为守护线程，那么意味着这个线程是“不重要”的，这意味着，如果主线程结束了而该守护线程还没有运行完，那么它将会被强制结束。

# 通过 setDaemon 方法来将某个线程设置为守护线程

import threading
import time

def target(second):
    print(f'Threading {threading.current_thread().name} is running')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')

print(f'Threading {threading.current_thread().name} is running')

t1 = threading.Thread(target=target, args=[2])
t1.start()
t2 = threading.Thread(target=target, args=[5])
t2.setDaemon(True)  # 通过 setDaemon 方法将 t2 设置为了守护线程，这样主线程在运行完毕时，t2 线程会随着线程的结束而结束
t2.start()

print(f'Threading {threading.current_thread().name} is ended')

# Threading MainThread is running
# Threading Thread-1 is running
# Threading Thread-1 sleep 2s
# Threading Thread-2 is running
# Threading MainThread is ended
#
# Threading Thread-2 sleep 5s
# Threading Thread-1 is ended

# 可以看到，没有看到 Thread-2 打印退出的消息，Thread-2 随着主线程的退出而退出了
# 这里并没有调用 join 方法，如果我们让 t1 和 t2 都调用 join 方法，主线程就会仍然等待各个子线程执行完毕再退出，不论其是否是守护线程