import multiprocessing as mp
from multiprocessing import Pool

global_result = 0

def taylor(x):
    global global_result
    global_result += 1/x
    return global_result

if __name__ == '__main__':
    mp.set_start_method('fork')
    with Pool(10) as p:
        print(p.map(taylor,range(1,1000)))
