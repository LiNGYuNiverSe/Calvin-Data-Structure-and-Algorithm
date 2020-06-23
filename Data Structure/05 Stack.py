# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 16:03:20 2020

@author: caoli
"""


class Stack(object):
    def __init__(self):
        #initialize a empty list
        self.__list = []
    
    def push(self, item):
        self.__list.append(item)
        #self.__list.add(item)
    def pop(self):
        return self.__list.pop()

    def peek(self):
        return self.__list[len(self.__list) - 1]
    
    def is_empty(self):
        return self.__list == []
        
    def size(self):
        return len(self.__list)
    


if __name__ =="__main__":
    stack = Stack()
    print("Is empty stack ---", stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Is empty stack ---", stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("Is empty stack ---", stack.is_empty())
