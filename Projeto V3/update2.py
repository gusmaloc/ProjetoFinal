from multiprocessing import Pool

global_result = 0

def taylor(x):
    global global_result
    global_result += 1/x
    return global_result

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(taylor,range(1,10)))
