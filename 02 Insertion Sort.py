# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:37:33 2020

@author: caoli
"""
alist = [9,3,5,7,2,10]

def insert_sort(alist):
    n = len(alist)
    for j in range(1,n): # the last one is n-1 and range(n) ends at n-1
        i = j #select the elem(index) we want to insert
        while i > 0: # compare with every elem in the ordered part from the end
            if alist[i] < alist[i-1]: # if current elem is less than the prev one, then switch
                alist[i], alist[i-1] = alist[i-1], alist[i]
            else: # if no need to switch, go compare next prev one
                break
            i-=1
    return alist

if __name__ =="__main__":
    print(insert_sort(alist))