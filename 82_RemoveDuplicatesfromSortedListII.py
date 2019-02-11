class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

def deleteDupliates(head):
    if head is None or head.next is None:
        return head
    tmp = ListNode(0)
    tmp.next = head
    pre = tmp
    q, p = head, head.next
    flag = 0
    while p:
        if p.val == q.val:
            q.next = p.next
            p = q.next
            flag = 1
        elif p.val != q.val and flag:
            pre.next = p
            q = p
            p = q.next
            flag = 0
        else:
            pre = q
            q = p
            p = p.next
    if flag:
        pre.next = q.next
    return tmp.next


def display(head):
    vals = []
    if not head:
        return None
    while head:
        vals.append(str(head.val))
        head = head.next
    print('->'.join(vals))


if __name__ == '__main__':
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(4, l4)
    l2 = ListNode(1, l3)
    l1 = ListNode(1, l2)
    l = ListNode(1, l1)
    display(l)
    l = deleteDupliates(l)
    display(l)
    m1 = ListNode(1)
    m = ListNode(1,m1)
    display(m)
    m = deleteDupliates(m)
    display(m)