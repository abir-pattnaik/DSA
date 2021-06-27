# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:56:45 2021

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


## traverse a linked list
node_travel=node_5

def traverse_node(head):
    
    while(head!=None):
        if head.next!=None:
            print(head.data,'-->',head.next.data)
        else:
            print(head.data)
        head=head.next
    
traverse_node(node_travel)    
    
