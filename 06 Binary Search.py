# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:04:03 2020

@author: caoli
"""

# use loop to implement binary search
def loop_binary_search(alist, v):
    n = len(alist)
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        # compare mid and v
        if alist[mid] == v:
            return True
        elif alist[mid] > v:
            end = mid - 1
        else:
            start = mid + 1
    return False 
    

def recursive_binary_search(alist,v):
    n = len(alist)
    mid = n//2
    if n==0:
        return False    
    if alist[mid] == v:
        return True
    elif alist[mid] < v:
        # if on the right side, search the right half of the list
        return recursive_binary_search(alist[mid+1:],v)
    else:
        return recursive_binary_search(alist[0:mid],v)


if __name__ =="__main__":
    alist = [1,2,3,4,5,6,7,8,9]
    print(loop_binary_search(alist,7))
    print(recursive_binary_search(alist,19))
     

