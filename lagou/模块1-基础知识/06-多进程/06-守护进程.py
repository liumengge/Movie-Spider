# 如果一个进程被设置为守护进程，当父进程结束后，子进程会自动被终止，我们可以通过设置 daemon 属性来控制是否为守护进程。

from multiprocessing import Process
import time

class MyProcess(Process):

    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid} LoopCount: {count}')

if __name__ == '__main__':

    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()

print('Main Process ended')

# 这样可以有效防止无控制地生成子进程。这样的写法可以让我们在主进程运行结束后无需额外担心子进程是否关闭，避免了独立子进程的运行。