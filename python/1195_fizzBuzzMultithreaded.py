#!/usr/bin/env python3
from threading import Lock, Thread

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.count = 1
        self.locks = (Lock(), Lock(), Lock(), Lock())
        self.locks[1].acquire()
        self.locks[2].acquire()
        self.locks[3].acquire()

    # printFizz() outputs "fizz"
    def printFizz(self):
        print("fizz")

    def changeLockStatus(self):
        #print("self.count:", self.count)
        if self.count > self.n:
            self.locks[0].release()
            self.locks[1].release()
            self.locks[2].release()
            self.locks[3].release()
        elif self.count%15 == 0:
            
            #print("self.count%15 == 0")
            self.locks[3].release()
        elif self.count%5 == 0:
            #print("self.count%5 == 0")
            self.locks[2].release()
        elif self.count%3 == 0:
            #print("self.count%3 == 0")
            self.locks[1].release()
        else:
            #print("self.count is not divisible by 3 or 5")
            self.locks[0].release()
        
        

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.n//3 - self.n//15):
            with self.locks[1]:
                printFizz()
                self.count += 1
                self.changeLockStatus()
                self.locks[1].acquire()

    	

    # printBuzz() outputs "buzz"
    def printBuzz(self):
        print("buzz")
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n//5-self.n//15):
            with self.locks[2]:
                printBuzz()
                self.count+=1
                self.changeLockStatus()
                self.locks[2].acquire()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def printFizzBuzz(self):
        print("fizzbuzz")
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.n//15):
            with self.locks[3]:
                printFizzBuzz()
                self.count+=1
                self.changeLockStatus()
                self.locks[3].acquire()
        

    # printNumber(x) outputs "x", where x is an integer.
    def printNumber(self,x):
        print(x)
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n - self.n//3  - self.n//5 + self.n//15):
            with self.locks[0]:
                printNumber(self.count)
                self.count+=1
                #print("in number:", self.count)
                self.changeLockStatus()
                self.locks[0].acquire()
                
        

if __name__ == "__main__":
    n = 15
    fb =  FizzBuzz(n)

    Thread(target=fb.number, args=(fb.printNumber,)).start()
    Thread(target=fb.fizz, args=(fb.printFizz,)).start()
    Thread(target=fb.buzz, args=(fb.printBuzz,)).start()
    Thread(target=fb.fizzbuzz, args=(fb.printFizzBuzz,)).start()
