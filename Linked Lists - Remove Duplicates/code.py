def remove_duplicates(head):
    if head is None:
        return head
    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head
