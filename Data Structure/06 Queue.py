# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:14:54 2020

@author: caoli
"""


class Queue(object):
    def __init__(self):        
        self.__list = []
        

    def enqueue(self,item):
        self.__list.append(item) # more enqueue than dequeue
        #self.__list.insert(0,item) # more dequeue than enqueue
        
    def dequeue(self):
        #return self.__list.pop(0)
        return self.__list.pop()
    
    def is_empty(self):
        return self.__list == []
    
    def size(self):
        return len(self.__list)
    
if __name__ =="__main__":
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.size())
    queue
    queue.dequeue()
    print(queue.dequeue())
    print(queue.dequeue())