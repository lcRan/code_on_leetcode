class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # 定义Node的字符输出，print为输出data
    def __repr__(self):
        return str(self.data)


class ListLink(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = None
        self.length = 0

    def append(self, data):
        q = Node(data)
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

    def getItem(self, index):
        if index >= self.length:
            return
        p = self.head
        while index > 0:
            p = p.next
            index -= 1
        return p.data

    def insert(self, data, index):
        q = Node(data)
        p = self.head
        if index > self.length:
            print('out of index')
            return
        while index > 0:
            p = p.next
            index -= 1
        q.next = p
        p.next = q

    def update(self, data, index):
        q = Node(data)
        p = self.head
        if index > self.length:
            print('out of index')
            return
        while index > 0:
            p = p.next
            index -= 1
        q.next = p
        p.next = q

if __name__ == '__main__':
    l = ListLink()
    data = [0, 3, 7, 8]
    for i in data:
        l.append(i)
    l.showlist()
    print(l.length)
    print(l.getItem(0))
    print(l.getItem(3))
    print(l.getItem(10))
    l.insert(4, 2)
    l.showlist()
    l.insert(-3, 0)
    l.showlist()
