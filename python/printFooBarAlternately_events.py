#!/usr/bin/env python3
from threading import Thread, Event
from time import sleep

'''
1115. Print FooBar Alternately
https://leetcode.com/problems/print-foobar-alternately/
'''

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.events = (Event(), Event())
        self.events[0].set()
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
            
            # printFoo() outputs "foo". Do not change or remove this line.
            #sleep(0.01)
                self.events[0].wait()
                printFoo()
                self.events[1].set()
                self.events[0].clear()


    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            self.events[1].wait()
            # printBar() outputs "bar". Do not change or remove this line.
            #sleep(0.01)
            printBar()
            self.events[0].set()
            self.events[1].clear()
                

if __name__ == "__main__" :
    fb = FooBar(3)
    Thread(target=fb.foo, args=(fb.printFoo,)).start()
    Thread(target=fb.bar, args=(fb.printBar,)).start()