# import multiprocessing
#
# def process(index):
#
#     print(f'Process: {index}')
#
# if __name__ == '__main__':
#
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,)) # target 参数传入方法名，args 是方法的参数，是以元组的形式传入，其和被调用的方法 process 的参数是一一对应的
#         # 这里 args 必须要是一个元组，如果只有一个参数，那也要在元组第一个元素后面加一个逗号，如果没有逗号则和单个元素本身没有区别，无法构成元组，导致参数传递出现问题
#         p.start()


import multiprocessing
import time
def process(index):
    time.sleep(index)
    print(f'Process: {index}')
if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=[i])
        p.start()
    print(f'CPU number: {multiprocessing.cpu_count()}')  # 获取 CPU 核心的数量
    for p in multiprocessing.active_children():  # 通过 active_children 获取当前正在活跃运行的进程列表
        print(f'Child process name: {p.name} id: {p.pid}')
    print('Process Ended')