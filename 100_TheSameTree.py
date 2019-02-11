class Node(object):
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = Node()

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.lchild is None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild is None:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.data == q.data:
                return self.isSameTree(p.lchild, q.lchild) and self.isSameTree(p.rchild, q.rchild)
            else:
                return False


if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(i)
    print(arr)