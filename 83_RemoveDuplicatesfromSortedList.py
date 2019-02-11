class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

def deleteDupliates(head):
    if not head:
        return None
    q, p = head, head.next
    while p:
        if p.val == q.val:
            q.next = p.next
            p = q.next
        else:
            q = p
            p = p.next
    return head


def display(head):
    vals = []
    if not head:
        return None
    while head:
        vals.append(str(head.val))
        head = head.next
    print('->'.join(vals))

  #  def deleteDupliates(self, head):


if __name__ == '__main__':
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(4, l4)
    l2 = ListNode(3, l3)
    l1 = ListNode(3, l2)
    l = ListNode(1, l1)
    display(l)
    deleteDupliates(l)
    display(l)