# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:47:03 2020

@author: caoli
"""


class Node(object):
    def __init__(self,elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None
    def add(self,elem):
        node = Node(elem)
        # root exists?
        if self.root == None:
            self.root = node
        else:           
            queue = []
            queue.append(self.root)
            while queue: # while != none
                curNode = queue.pop(0)
                if curNode.lchild == None:
                    curNode.lchild = node
                    return # end loop
                else:
                    queue.append(curNode.lchild)
                if curNode.rchild == None:
                    curNode.rchild = node
                    return # end loop
                else:
                    queue.append(curNode.rchild)
    

    def travel(self):
        queue = []
        if self.root is None:
            return 
        else:
            queue.append(self.root)
        while queue:
            curNode = queue.pop(0)
            print(curNode.elem, end="\t")
            if curNode.lchild is not None:
                queue.append(curNode.lchild)
            if curNode.rchild is not None:
                queue.append(curNode.rchild)
    
    def preOrder(self,root):
        """Recursion
            root - lchild - rchild"""
        if root is None:
            return
        else:
            print(root.elem, end="\t")
            self.preOrder(root.lchild)
            self.preOrder(root.rchild)
    
    def inOrder(self,root):
        if root is None:
            return 
        else:
            self.inOrder(root.lchild)
            print(root.elem, end="\t")
            self.inOrder(root.rchild)

    def lastOrder(self,root):
        if root is None:
            return 
        else:
            self.lastOrder(root.lchild)
            self.lastOrder(root.rchild)
        print(root.elem, end="\t")


                    
if __name__=="__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("Breadth-First Search")
    tree.travel()
    print("preOrder Search")
    tree.preOrder(tree.root)
    print("inOrder Search")
    tree.inOrder(tree.root)
    print("lastOrder Search")      
    tree.lastOrder(tree.root)