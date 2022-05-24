import multiprocessing as mp
from multiprocessing import Process, Queue

global_result = 0
num_subProcess = 4
start = 1
end = 250

def taylor(start_num, end_num, q):
    global global_result
    T = start_num
    while T <= end_num:
        global_result += 1/T
        T += 1
    q.put(global_result)

if __name__ == '__main__':
    mp.set_start_method('spawn')
    q = mp.Queue()
    for i in range(num_subProcess):
        p = mp.Process(target = taylor, args=(start,end,q))
        p.start()
        print("\nResultados: ", q.get())
        start += 250
        end += 250

 
    p.join()
    print("\nResultados: ",  q.get())


    

#def foo(q):
 #   q.put('hello')

  #  q = mp.Queue()
   # p = mp.Process(target=foo, args=(q,))
   # p.start()
    #print(q.get())
    #p.join()
