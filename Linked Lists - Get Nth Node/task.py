# from preloaded import Node

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if not node:
        raise IndexError("None linked list should throw error.")
    current = node
    try:
        i = 0
        while True:
            if i == index:
                return Node(current.data)
            current = current.next
            i += 1
    except AttributeError:
        raise IndexError("Invalid index value should throw error.")
