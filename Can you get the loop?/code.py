def loop_size(node):
    fast = node
    slow = node
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = slow.next
            count = 1
            while slow != fast:
                count += 1
                slow = slow.next
            return count
    return None
