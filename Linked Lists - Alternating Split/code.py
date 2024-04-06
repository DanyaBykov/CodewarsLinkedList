def alternating_split(head):
    first = []
    second = []
    count = 1
    while head:
        if count % 2 == 1:
            first.append(head.data)
        else:
            second.append(head.data)
        head = head.next
        count += 1
    first_data = Node(first[0])
    temp = first_data
    for i in range(1, len(first)):
        temp.next = Node(first[i])
        temp = temp.next
    second_data = Node(second[0])
    temp = second_data
    for i in range(1, len(second)):
        temp.next = Node(second[i])
        temp = temp.next
    return Context(first_data, second_data)
