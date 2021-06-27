# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:55:57 2021

@author: abirp
"""

##create a new node
class Node:
    def __init__ (self,data,next=None):
        self.data=data
        self.next=next
        

## create a linked list
node=Node(3)
node_1=Node(4,node)
node_2=Node(5,node_1)
node_3=Node(2,node_2)
node_4=Node(7,node_3)
node_5=Node(9,node_4)


##Adding node in the beginning
head=Node(10,node_5)

## traverse a linked list
node_travel=head


while(node_travel!=None):
    if node_travel.next!=None:
        print(node_travel.data,'-->',node_travel.next.data)
    else:
        print(node_travel.data)
    node_travel=node_travel.next
    