#!/usr/bin/env python3
"""
atds.py
stack
"""

__author__ = "Niko Vidalaks"
__version__ = "January 17 2023"

class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
       return self.stack.pop() 
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class Queue(object):
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
class Deque(object):
    def __init__(self):
        self.queue = []
    def add_front(self,item):
        self.queue.insert(0,item)
    def add_rear(self,item):
        self.queue.append(item)
    def remove_front(self):
        return self.queue.pop(0)
    def remove_back(self):
        return self.queue.pop()
    def size(self):
        return len(self.queue)
    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def to_string(self):
        return_string = ''
        for i in self.queue:
            return_string += str(i)
        return return_string
        

