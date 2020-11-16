from multiprocessing import Process
import time

class MyProcess(Process):

    def __init__(self, loop):  # loop代表循环次数，并设置为全局变量
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid} LoopCount: {count}')

if __name__ == '__main__':

    for i in range(2, 5):
        p = MyProcess(i)
        p.start()
