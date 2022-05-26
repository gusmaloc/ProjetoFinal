import multiprocessing as mp
from multiprocessing import Pool
from functools import reduce

global_result = 0

def taylor(x):
    return 1/x

if __name__ == '__main__':
    mp.set_start_method('spawn')
    with Pool(10) as p:
        global_result = p.map(taylor,range(1,1000))
    result = reduce(lambda x,y: x+y ,global_result)

    print("resultado: ", result)
