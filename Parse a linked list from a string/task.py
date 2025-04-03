class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s == "None" or not s.strip():
        return None

    nodes = s.split(" -> ")[:-1]

    if not nodes or not nodes[0].strip():
        return None

    head = Node(int(nodes[0]))
    current = head

    for val in nodes[1:]:
        try:
            current.next = Node(int(val))
            current = current.next
        except ValueError:
            return None

    return head
