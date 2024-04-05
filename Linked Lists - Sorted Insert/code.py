def sorted_insert(head, data):
    if head is None:
        return Node(data)
    listy = []
    while head:
        listy.append(head.data)
        head = head.next
    listy.append(data)
    listy.sort()
    head = Node(listy[0])
    current = head
    for i in range(1, len(listy)):
        current.next = Node(listy[i])
        current = current.next
    return head
