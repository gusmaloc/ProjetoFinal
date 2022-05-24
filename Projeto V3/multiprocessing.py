
import multiprocessing

global_result = 0

def taylor(start_num, end_num):
    global global_result
    T = start_num
    while T <= end_num:
        global_result += 1/T
        T += 1




p1 = multiprocessing.Process(target = taylor(1,250))
p2 = multiprocessing.Process(target = taylor(251,500) )
p3 = multiprocessing.Process(target = taylor(501,750))
p4 = multiprocessing.Process(target = taylor(751,1000))
    
p1.start()
p2.start()
p3.start()
p4.start()
    
p1.join()
p2.join()
p3.join()
p4.join()

print("\nResultados: ", global_result)
