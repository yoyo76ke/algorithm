#!/usr/bin/env python3
from threading import Thread, Condition
from time import sleep

'''
1115. Print FooBar Alternately
https://leetcode.com/problems/print-foobar-alternately/
'''

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.cond = Condition()
        self.order = 0
        self.fooTurn = lambda: self.order == 0
        self.barTurn = lambda: self.order == 1

    def printFoo(self):
        print("foo")

    def printBar(self):
        print("bar")

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in range(self.n):
            with self.cond:
                self.cond.wait_for(self.fooTurn)
            # printFoo() outputs "foo". Do not change or remove this line.
            #sleep(0.01)
                printFoo()
                self.order = 1
                self.cond.notify()
                



    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            with self.cond:
                print(self.barTurn)
                self.cond.wait_for(self.barTurn)
            # printBar() outputs "bar". Do not change or remove this line.
            #sleep(0.01)
                printBar()
                self.order = 0
                if i != (self.n -1):
                    self.cond.notify()

                

if __name__ == "__main__" :
    fb = FooBar(3)
    Thread(target=fb.foo, args=(fb.printFoo,)).start()
    Thread(target=fb.bar, args=(fb.printBar,)).start()