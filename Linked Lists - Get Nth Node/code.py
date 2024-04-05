def get_nth(node, index):
    if node is None:
        raise ValueError
    if index < 0:
        raise ValueError
    while index:
        if node.next is None:
            raise ValueError
        node = node.next
        index -= 1
    return node
