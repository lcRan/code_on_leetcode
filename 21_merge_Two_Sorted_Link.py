class ListNode(object):
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


def mergeTwoLists (l1, l2):
    if not (l1 or l2):
        return None
    if not l1:
        return l2
    if not l2:
        return l1

    l, p = None, None
    if l1.val < l2.val:
        l, p = l1, l1
        l1 = l1.next
    else:
        l, p = l2, l2
        l2 = l2.next
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next
    if l1:
        p.next = l1
    if l2:
        p.next = l2
    return l


def display (head):
    vals = []
    if not head:
        return None
    while head:
        vals.append(str(head.val))
        head = head.next

    print('->'.join(vals))



l_5 = ListNode (5)
l_4 = ListNode (4, l_5)
l1 = ListNode (1, l_4)
l_3 = ListNode (3)
l_2 = ListNode (2, l_3)
l2 = ListNode (1,l_2)
display (l1)
display(l2)
l = mergeTwoLists(l1, l2)
display(l)
