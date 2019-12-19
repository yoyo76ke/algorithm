#!/usr/bin/env python3

from threading import Thread, Lock

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.locks = (Lock(), Lock(), Lock())
        if n >= 1:
            self.locks[1].acquire()
        if n >= 2:
            self.locks[2].acquire()
        
    def printNumber(self,x):
        print(x)
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            self.locks[0].acquire()
            printNumber(0)
                
            if (i+1)%2 == 0:
                self.locks[2].release()
            else:
                self.locks[1].release()   
            
                    
                 
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n//2):
            self.locks[2].acquire()
            printNumber(2*i+2)
            self.locks[0].release()
                    


        
    
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range((self.n+1)//2):
            self.locks[1].acquire()
            printNumber(2*i+1)
            self.locks[0].release()
                    


        
if __name__ == "__main__":
    i = 0
    n = 4
    zeo = ZeroEvenOdd(n)

    Thread(target=zeo.zero, args=(zeo.printNumber,)).start()
    Thread(target=zeo.even, args=(zeo.printNumber,)).start()
    Thread(target=zeo.odd, args=(zeo.printNumber,)).start()

    
