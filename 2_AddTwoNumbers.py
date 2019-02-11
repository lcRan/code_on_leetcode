# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode:
    def __init__(self, x):
        self.data = x
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def append(self, data):
        q = ListNode(data)
        if self.head == None:
            self.head = q
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = q
        self.length += 1

    def showlist(self):
        val = []
        if self.head == None:
            return
        p = self.head
        while p.next:
            val.append(str(p.data))
            p = p.next
        val.append(str(p.data))
        print('->'.join(val))

    def getNumber(self):
        number = 0
        if self.head == None:
            return 0
        p = self.head
        while p.next:
            number = number * 10 + p.data
            p = p.next
        number = number * 10 + p.data
        return number

    def addTwoNumbers(self, l1, l2):
        number1 = l1.getNumber()
        number2 = l2.getNumber()
        result = number1 + number2
        l = LinkList()
        while result:
            data = result % 10
            l.append(data)
            result = result // 10
        return l


if __name__ == '__main__':
    l1 = LinkList()
    l2 = LinkList()
    l3 = LinkList()
    data1 = [2, 4, 3]
    data2 = [5, 6, 4]
    for data in data1:
        l1.append(data)
    l1.showlist()
    for data in data2:
        l2.append(data)
    l2.showlist()
    l3 = l3.addTwoNumbers(l1, l2)
    l3.showlist()

