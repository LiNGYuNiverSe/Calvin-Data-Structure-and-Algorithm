# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:26:44 2020

@author: caoli
"""


def merge_sort(alist):
    #split //2
    n = len(alist)
    if n<=1:
        return alist
    mid = n//2
    left_li  = merge_sort(alist[0:mid])
    right_li = merge_sort(alist[mid:])
    #merge
    result = []
    left_pointer, right_pointer = 0,0
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    #when exit while loop, append the rest elements of not null list to the result
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]        
    return  result

def merge_sort1(alist):
    #split //2
    n = len(alist)
    if n<=1:
        return alist
    mid = n//2
    left_li  = merge_sort(alist[0:mid])
    right_li = merge_sort(alist[mid:])
    print(left_li,right_li)

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    print("Original list:")
    print(alist)
    print("Ordered list:")
    print(merge_sort(alist))
    
