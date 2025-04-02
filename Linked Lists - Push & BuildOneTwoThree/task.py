# from preloaded import Node

'''
Node is defined in preloaded like this:
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


def push(head, data):
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    n3 = Node(3)
    n2 = Node(2)
    n2.next = n3
    n1 = Node(1)
    n1.next = n2
    return n1
