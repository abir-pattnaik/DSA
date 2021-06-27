# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:56:45 2021

@author: abirp
"""

class Node:
    def __init__ (self,data,next=None):
        self.data=data
        self.next=next
        

## create a single node
node=Node(3)

print(node.data)
