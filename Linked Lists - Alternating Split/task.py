class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head:
        raise ValueError()

    f = head
    s = head.next
    f_cur = f
    s_cur = s
    current = head.next.next

    i = 1
    while current:
        if i % 2 == 0:
            s_cur.next = current
            s_cur = s_cur.next
        else:
            f_cur.next = current
            f_cur = f_cur.next
        i += 1
        current = current.next

    f_cur.next = None
    s_cur.next = None

    return Context(f, s)
