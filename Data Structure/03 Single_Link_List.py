# -*- coding: utf-8 -*-
"""
Single Link List
#method:
    is_empty(),
    length(),
    travel(),
    add(),
    append(),
    insert(),
    search(),    
@author: Calvin Cao
"""

# Node is the unit of the list 
class Node(object):
    def __init__(self,elem):
        #store element
        self.elem = elem
        #find the next node, default is None
        self.next = None
        
class SingleLinkList():
    def __init__(self,node= None): # so that we can make empty singlelinklist
        if node != None:
            headNode = Node(node)
            self.__head = headNode
        else:
            self.__head = node 
                
    def add(self,item):
        #convert new item to node first
        node=Node(item)
        #link 
        node.next = self.__head
        self.__head = node
        
    def append(self, item):
        node = Node(item)
        if self.is_empty(): # if self.__head is None, self.__head.next doesn't exist 
            self.__head = node
        else:        
            curNode = self.__head
            while curNode.next != None:#beware, .next can let the while loop stop at the last node, instead of the None 
                curNode = curNode.next
            curNode.next = node
            
    def insert(self, pos, item):
        if pos <0:
            self.add(item)
        elif pos >(self.length()-1):
            self.append(item)
        else:    
            count = 0 
            preNode = self.__head
            node = Node(item)
            while count < (pos-1): # find the prev node
                count += 1
                preNode = preNode.next # think .next as what behind the current node            
            node.next = preNode.next
            preNode.next = node
    
    def remove(self,item):
        curNode = self.__head
        preNode = None
        while curNode != None:
            if curNode.elem == item:                   
                if preNode == None: # if curNode is head, because head has no .next 
                    self.__head = curNode.next
                else:
                    preNode.next = curNode.next
                break

            else:
                preNode = curNode
                curNode = curNode.next


    def search(self,item):
        curNode = self.__head
        while curNode != None:
            if curNode.elem == item:
                return True
            curNode =curNode.next
        return False
    
    def is_empty(self):
        return self.__head == None
    
    def length(self):
        count = 0
        curNode= self.__head
        while curNode != None:
            count += 1
            curNode = curNode.next
        return count
    
    def travel(self):
        curNode = self.__head
        while curNode != None:
            print(curNode.elem, end="\t")
            curNode = curNode.next
        print("")
    
if __name__ =="__main__":
   #initialize a node
   singleLinkList = SingleLinkList(20)
   singleLinkList1 = SingleLinkList()
   print("Is empty:", singleLinkList.is_empty())
   print("Is empty:", singleLinkList1.is_empty())
   print("Length:", singleLinkList.length())
   print("Travel:", singleLinkList.length())
   print("Travel:", singleLinkList1.length())
   print("Search20",singleLinkList.search(20))
   print("Search30",singleLinkList.search(30))
   print("------Add------")
   singleLinkList.add(1)
   singleLinkList.add(2)
   singleLinkList.add(3)
   singleLinkList.travel()
   print("------Append------")   
   singleLinkList.append(10)
   singleLinkList.append(20)
   singleLinkList.append(30)
   singleLinkList.travel()
   print("------Insert------")
   singleLinkList.insert(2,200)
   singleLinkList.insert(100,300)
   singleLinkList.insert(-1,100)
   singleLinkList.travel()
   print("------Remove------")
   singleLinkList.remove(300)
   singleLinkList.remove(200)
   singleLinkList.remove(100)
   singleLinkList.travel()