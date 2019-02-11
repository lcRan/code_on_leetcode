class Node(object):
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = Node()

    def add(self, data):
        node = Node(data)
        if self.isEmpty():
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

    def pre_order(self, start):
        node = start
        if node == None:
            return
        print(node.data)
        if node.lchild == None and node.rchild == None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, start):
        node = start
        if node == None:
            return
        self.in_order(node.lchild)
        print(node.data)
        self.in_order(node.rchild)

    def post_order(self, start):
        node = start
        if node == None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.data)

    def level_order(self):
        node = self.root
        if node == None:
            return
        queue = []
        queue.append(node)
        while queue:
            node = queue.pop()
            print(node.data)
            if node.rchild:
                queue.append(node.rchild)
            if node.lchild:
                queue.append(node.lchild)
        print()

    def isEmpty(self):
        return True if self.root.data == -1 else False


if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append(i)
    print(arr)

    tree = BinaryTree()
    for i in arr:
        tree.add(i)

    print('Level_order:')
    tree.level_order()
    print('Pre_order:')
    tree.pre_order(tree.root)
    print('In_order:')
    tree.in_order(tree.root)
    print('Post_order:')
    tree.post_order(tree.root)
