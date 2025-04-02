class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    result = []
    if node is None:
        return 'None'
    while True:
        result.append(str(node.data))
        if node.next is None:
            result.append(str(node.next))
            break
        node = node.next
    
    return ' -> '.join(result)
