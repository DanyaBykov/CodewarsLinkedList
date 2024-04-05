def linked_list_from_string(s):
    if s == "None":
        return None
    s = s.split(" -> ")
    s = s[:-1]
    s = list(map(int, s))
    s.reverse()
    head = Node(s[0])
    for i in range(1, len(s)):
        head = Node(s[i], head)
    return head
