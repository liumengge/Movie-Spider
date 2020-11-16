# 假如现在我们遇到这么一个问题，我有 10000 个任务，每个任务需要启动一个进程来执行，并且一个进程运行完毕之后要紧接着启动下一个进程，
# 同时我还需要控制进程的并发数量，不能并发太高，不然 CPU 处理不过来（如果同时运行的进程能维持在一个最高恒定值当然利用率是最高的）

# Pool 可以提供指定数量的进程，供用户调用，当有新的请求提交到 pool 中时，
# 如果池还没有满，就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来执行它。


from multiprocessing import Pool
import time

def function(index):

    print(f'Start process: {index}')
    time.sleep(3)
    print(f'End process {index}', )

if __name__ == '__main__':

    pool = Pool(processes=3)  # 声明了一个大小为 3 的进程池，通过 processes 参数来指定，如果不指定，那么会自动根据处理器内核来分配进程数
    for i in range(4):
        pool.apply_async(function, args=(i,))  # 使用 apply_async 方法将进程添加进去，args 可以用来传递参数。
    print('Main Process started')
    pool.close()
    pool.join()
    print('Main Process ended')




