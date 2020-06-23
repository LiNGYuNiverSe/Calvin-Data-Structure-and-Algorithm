# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:57:12 2020

@author: caoli
"""


from timeit import Timer

def append_test():
    li = []
    for i in range(10000):
        li.append(i) #O(1)


def insert_test():
    li = []
    for i in range(10000):
        li.insert(0,i) #O(n)



append_timer = Timer("append_test()",
                     "from __main__ import append_test")
print("Append time:", append_timer.timeit(1000))# run 10k and get the avg running time


insert_timer = Timer("insert_test()",
                     "from __main__ import insert_test")
print("Insert time:",insert_timer.timeit(1000))        