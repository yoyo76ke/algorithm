#!/usr/bin/env python3
from threading import Thread, Lock
from time import sleep

'''
1115. Print FooBar Alternately
https://leetcode.com/problems/print-foobar-alternately/
'''


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.locks = (Lock(), Lock())
        self.locks[1].acquire()
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
            with self.locks[0]:
            # printFoo() outputs "foo". Do not change or remove this line.
            #sleep(0.01)
                printFoo()
                self.locks[1].release()
                if i != (self.n - 1):
                    self.locks[0].acquire()
                #self.locks[1].release()



    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in range(self.n):
            with self.locks[1]:
            # printBar() outputs "bar". Do not change or remove this line.
            #sleep(0.01)
                printBar()
                if i != (self.n - 1):
                    self.locks[0].release()
                    self.locks[1].acquire()
                



if __name__ == "__main__" :
    fb = FooBar(3)
    Thread(target=fb.foo, args=(fb.printFoo,)).start()
    Thread(target=fb.bar, args=(fb.printBar,)).start()