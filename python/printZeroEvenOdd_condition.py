#!/usr/bin/env python3

from threading import Thread, Condition, currentThread

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.cond = Condition()
        self.order = 2
        self.isZero = lambda: self.order == 2
        self.isEven = lambda: self.order == 0
        self.isOdd = lambda: self.order == 1


        
    def printNumber(self,x):
        print(x)
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n):
            with self.cond:
                
                self.cond.wait_for(self.isZero)
                printNumber(0)
                if (i+1)%2 == 0:
                    self.order = 0
                else:
                    self.order = 1 
                self.cond.notify(2)

        
                 
        
    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(self.n//2):
            with self.cond:
               
                self.cond.wait_for(self.isEven)
                printNumber(2*i+2)
                self.order = 2
                self.cond.notify(2)
                
                
        


        
    
    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range((self.n+1)//2):
            with self.cond:
                
                self.cond.wait_for(self.isOdd)
                printNumber(2*i+1)
                self.order = 2
                self.cond.notify(2)
                
       
        
if __name__ == "__main__":
    i = 0
    n = 0
    zeo = ZeroEvenOdd(n)

    Thread(target=zeo.zero, args=(zeo.printNumber,)).start()
    Thread(target=zeo.even, args=(zeo.printNumber,)).start()
    Thread(target=zeo.odd, args=(zeo.printNumber,)).start()

    
