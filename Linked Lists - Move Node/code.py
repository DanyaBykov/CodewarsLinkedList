def move_node(source, dest):
    if source is None:
        raise ValueError
    else:
        new_node = Node(source.data)
        new_node.next = dest
        dest = new_node
        source = source.next
        return Context(source, dest)
