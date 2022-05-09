import _thread

num_thread = 0
global soma
thread_started = False

def taylor(max_loop, num_min):
    global num_thread, thread_started, soma
    thread_started = True
    num_thread += 1
    while num_min <= max_loop:
        soma += 1/num_min
        num_min += 1
    num_thread -= 1

soma = 0        
_thread.start_new_thread(taylor, (500, 1))
_thread.start_new_thread(taylor, (1000, 501))

while not thread_started:
    pass

print("Soma durante o processo: ", soma)
 
while num_thread > 0:
    pass

print("Soma final: ", soma)
