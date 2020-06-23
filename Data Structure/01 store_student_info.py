# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:21:15 2020

@author: caoli
"""

# use list store student info
#list with tuple
stus=[("1001","Calvin",26,100),
      ("1002","Lingyu",23,98)]
# list with dict
stus=[{"sno":1001,"sname":"Calvin","age":26,"score": 100},
      {"sno":1002,"sname":"Lingyu","age":23,"score": 98}]

# use loop to get a specific student info - time effience O(n)
for stu in stus:
    pass

# however if use dict with keys, the time efficency will be O(1)

stus = {"1001":{"sname": "Calvin","age":26,"score":100},
        "1002":{"sname":"Lingyu","age":23,"score":98}}

from timeit import Timer
def append_list():
    li=[]
    for i in range(10000):
        li.append(i)
        
def insert_test():
    li = []
    for i in range(10000)：:
        li.insert(i,0)