#!/usr/bin/env python3
from threading import Thread, Condition
'''
1114. Print in Order
https://leetcode.com/problems/print-in-order/
'''

class Foo(object):
    def __init__(self):
        self.exec_condition = Condition()
        self.order = 0
        self.first_finish = lambda: self.order == 1
        self.second_finish = lambda: self.order == 2


    def printFirst(self):
        print("First")

    def printSecond(self):
        print("Second")

    def printThird(self):
        print("Third")

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        with self.exec_condition:
            printFirst()
            self.order = 1
            self.exec_condition.notify(2)



    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.exec_condition:
            self.exec_condition.wait_for(self.first_finish)

            printSecond()
            self.order = 2 
            self.exec_condition.notify()

            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.exec_condition:
            self.exec_condition.wait_for(self.second_finish)
            printThird()
            



def GetFuncName(l,ll, order):
    orderList = []
    funcNameList = []
    for i in order:
        orderList.append(l[i-1])
        funcNameList.append(ll[i-1])

    return orderList, funcNameList

if __name__ == "__main__" :
    f = Foo()
    l = [f.printFirst, f.printSecond, f.printThird]
    ll = [f.first, f.second, f.third]
    iList = [1, 3, 2]
    orderList, funcName = GetFuncName(l,ll, iList)
    '''
    f.first(f.printSecond)
    f.second(f.printFirst)
    f.third(f.printThird)
    '''
    
    Thread(target=funcName[0], args = (orderList[0],)).start()
    Thread(target=funcName[1], args = (orderList[1],)).start()
    Thread(target=funcName[2], args = (orderList[2],)).start()


