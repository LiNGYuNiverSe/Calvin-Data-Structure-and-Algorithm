# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:20:49 2020

@author: caoli
"""


def bubble_sort(alist):
    n = len(alist)
    for k in range(n-1):
        for i in range(n-1-k):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

    return alist

alist = [9,3,5,7,2,1]

print(bubble_sort(alist))

# improve

def bubble_sort_imp(alist):
    n = len(alist)
    count = 0
    for k in range(n-1):
        for i in range(n-1-k):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count +=1
        if count ==0:
            break

    return alist

print(bubble_sort_imp(alist))
