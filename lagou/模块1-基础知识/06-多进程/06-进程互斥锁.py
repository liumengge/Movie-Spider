# 在上面的一些实例中，我们可能会遇到如下的运行结果：

# Pid: 73993 LoopCount: 0
# Pid: 73993 LoopCount: 1
# Pid: 73994 LoopCount: 0Pid: 73994 LoopCount: 1
# Pid: 73994 LoopCount: 2
# Pid: 73995 LoopCount: 0
# Pid: 73995 LoopCount: 1
# Pid: 73995 LoopCount: 2
# Pid: 73995 LoopCount: 3
# Main Process ended

# 有的输出结果没有换行。这是什么原因造成的呢？
#     这种情况是由多个进程并行执行导致的，两个进程同时进行了输出，结果第一个进程的换行没有来得及输出，第二个进程就输出了结果，导致最终输出没有换行。
#     那如何来避免这种问题？如果我们能保证，多个进程运行期间的任一时间，只能一个进程输出，其他进程等待，等刚才那个进程输出完毕之后，另一个进程再进行输出，这样就不会出现输出没有换行的现象了。

# 进程互斥，避免了多个进程同时抢占临界区（输出）资源。我们可以通过 multiprocessing 中的 Lock 来实现。
# Lock，即锁，在一个进程输出时，加锁，其他进程等待。等此进程执行结束后，释放锁，其他进程可以进行输出。

#
from multiprocessing import Process, Lock
import time

class MyProcess(Process):

    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print(f'Pid: {self.pid} LoopCount: {count}')
            self.lock.release()

if __name__ == '__main__':

    lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()

