# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:13:57 2018

@author: Anannya
"""

class queue:
    def __init__(self):
        self.item=[0]
        
    def isEmpty(self):
        return self.item==[]
    
    def size(self):
        return len(self.item)
    
    def enqueue(self,item):
        self.item.insert(len(self.item),item)
        
    def dequeue(self):
        return self.item.pop(0)
    
    def __str__(self):
        return str(self.item)
queue = queue()
print('isEmpty():', queue.isEmpty())
print('empty:', queue)
queue.enqueue(10)
print('after enqueue(10):', queue)
print('isEmpty():', queue.isEmpty())
queue.enqueue(1)
print('after enqueue(1):', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
queue.enqueue(2)
print('after enqueue(2):', queue)
queue.enqueue(3)
print('after enqueue(3):', queue)
queue.enqueue(4)
print('after enqueue(4):', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('dequeue():', queue.dequeue())
print('after dequeue():', queue)
print('isEmpty():', queue.isEmpty())
        