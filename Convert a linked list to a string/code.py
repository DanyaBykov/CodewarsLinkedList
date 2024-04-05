def stringify(node):
    res = ""
    arrow = " -> "
    while node:
        res += str(node.data) + arrow
        node = node.next
    res += "None"
    return res
