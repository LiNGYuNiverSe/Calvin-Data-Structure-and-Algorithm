# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:14:40 2020

@author: caoli
"""
def quick_sort(alist,start,end):
    if start >= end:
        return alist
    #find a Benchmark to start with
    mid = alist[start]
    low = start
    high = end
    # from left to right, compare each elem with mid
    
    while low < high:
        while low < high and alist[high] > mid:
            high -=1
        alist[low] = alist[high]
        # from right to left
        while low < high and alist[low] < mid:
            low +=1
        alist[high] = alist[low]
    
    alist[low] = mid # now we find the position of Benchmark
    
    quick_sort(alist,start, low-1)
    quick_sort(alist, low +1, end)


def quick_sort_wrong(alist, start, end):
    #Recursion
    if start >= end:
        return alist
    mid = alist[0]
    low = 0 #low pointer
    high  = len(alist) - 1 #high pointer
    
    """from the right to the left, 
    if alist[high] > mid, 
    then high -= 1"""
    while low<high:
        
        while low < high and alist[high] > mid:
            high -= 1
        # Assign high's value to low
        alist[low] = alist[high]
        
        """from the left to the right,
        if alist[low] < mid, 
        then low += 1"""
        while low < high and alist[low] < mid:
            mid +=1
        
        alist[high] = alist[low]
    #put mid to the corresponding position
        alist[low] = mid
        """for all the low values on the left hand side,
        call the function repeatly"""
        quick_sort(alist, start, low-1)
        """for all the high values on the right hand side,
        call the function repeatly"""
        quick_sort(alist, low+1, end)
    return alist

if __name__== "__main__":
    alist= [54,26,93,17,77,31,44,55,20]
    print("Original array:")
    print(alist)
    print("Sorted array:")
    quick_sort(alist,0, len(alist)-1)
    print(alist)
    
    