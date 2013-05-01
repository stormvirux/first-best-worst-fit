from random import randint
from time import sleep

from gl import *
from hole import *
from process import *

def init():
    h = Hole(0, total_size)
    hole_list.append(h)
    for i in range(0, num_process):
        size = randint(1, max_psize)
        time = randint(1, max_ptime)
        p = Process(i + 1, size, time)
        process_queue.append(p)

def first_fit(p):
    for h in hole_list:
        if p.size <= h.length:
            p.addr = h.base
            print '''process %d start with %d - %d, 
            time:%d''' %(p.pid, p.addr, p.addr + p.size, p.time)
            
            if p.size < h.length:
                newh = Hole(h.base + p.size, h.length - p.size)
                hole_list.append(newh)
            hole_list.remove(h)
            p.start()
            return True
    else:
        return False
    
def main():
    init()
    for p in process_queue:
        while True:
            if first_fit(p):
                break
    for p in process_queue:
        p.join()
        process_queue.remove(p)
    print 'end'
    
if __name__ == "__main__":
    main()
