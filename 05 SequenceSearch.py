# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:54:47 2020

@author: caoli
"""
def sequence_search(alist,v):
    for i in range(len(alist)):# get the index of element
        if alist[i]==v:
            return i 
    # not found
    return -1
        
    
    
if __name__=="__main__":
    alist=[4,3,5,1,233,66,99]
    idx = sequence_search(alist, 99)
    if idx != -1:
        print("Valve found, the index is:", idx)
    else:
        print("not found")
    

