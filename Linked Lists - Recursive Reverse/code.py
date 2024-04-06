def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head
    new_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return new_head
