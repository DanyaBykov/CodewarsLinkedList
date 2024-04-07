def swap_pairs(head):
    res = Node(head)
    prev = res
    while prev.next and prev.next.next:
        a = prev.next
        b = prev.next.next
        prev.next= b
        a.next = b.next
        b.next = a
        prev = a
    return res.next
