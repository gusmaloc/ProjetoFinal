import _thread
from threading import*

obj = Semaphore(2)
num_thread = 4
swift = 0
start = 1
end = 250
global global_result
thread_started = False
global_result = 0

def taylor(start_num, end_num):
    global thread_started, swift, global_result
    thread_started = True
    T = start_num
    swift += 1
    obj.acquire()
    while T <= end_num:
        global_result += 1/T
        T += 1
        obj.release()
    swift -= 1
        
for i in range(num_thread):
    _thread.start_new_thread(taylor, (start, end))
    start += 250
    end += 250

while not thread_started:
    pass

print("Resultado Parcial: ", global_result)

while swift > 0:
    pass

print("\nResultados: ", global_result)
