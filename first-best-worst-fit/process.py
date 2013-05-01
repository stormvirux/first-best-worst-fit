from threading import Thread
from time import sleep

from gl import *
from hole import *

class Process(Thread):
    pid = 0
    size = 0
    time = 0
    addr = 0
    
    def __init__(self, pid, size, time):
        Thread.__init__(self)
        self.pid = pid
        self.size = size
        self.time = time
        self.addr = 0
        
    def __del__(self):
        pass

    def run(self):
        while self.time >= 0:
            sleep(1)
            base = self.addr
            length = self.size
            i = 0
            while i < len(hole_list):
                if (base + length) == hole_list[i].base:
                    length += hole_list[i].length
                    i = 0
                    continue
                i += 1
            h = Hole(base, length)
            hole_list.append(h)
            self.time -= 1
            
