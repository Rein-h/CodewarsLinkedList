def loop_size(node):
    current = node
    visited = {}
    counter = 0

    while True:
        if current.next in visited:
            break
        visited[current.next] = counter
        current = current.next
        counter += 1

    return counter - visited[current.next]
