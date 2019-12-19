#!/usr/bin/env python3

from threading import Thread, Event

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.events = (Event(), Event(), Event())
        self.events[0].set()
        
    def printNumber(self,x):
        print(x)
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            self.events[0].wait()
            printNumber(0)
            if (i+1)%2 == 0:
                self.events[2].set()
            else:
                self.events[1].set()  
            self.events[0].clear()
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n//2):
            self.events[2].wait()
            printNumber(2*i+2)
            self.events[0].set()
            self.events[2].clear()
    
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range((self.n+1)//2):
            self.events[1].wait()
            printNumber(2*i+1)
            self.events[0].set()
            self.events[1].clear()
                    
        
if __name__ == "__main__":
    i = 0
    n = 2
    zeo = ZeroEvenOdd(n)

    Thread(target=zeo.zero, args=(zeo.printNumber,)).start()
    Thread(target=zeo.even, args=(zeo.printNumber,)).start()
    Thread(target=zeo.odd, args=(zeo.printNumber,)).start()

    
