import random

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.rotations = 0

    def insert_key(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            self.rotations += 1
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            self.rotations += 1
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            self.rotations += 2
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            self.rotations += 2
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

class RBNode:
    def __init__(self, key, color='red'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RBTree:
    def __init__(self):
        self.TNULL = RBNode(0, 'black')
        self.root = self.TNULL
        self.rotations = 0

    def insert(self, key):
        node = RBNode(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = 'black'
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                        self.rotations += 1
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._left_rotate(k.parent.parent)
                    self.rotations += 1
            else:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                        self.rotations += 1
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._right_rotate(k.parent.parent)
                    self.rotations += 1
            if k == self.root:
                break
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

# Generate large dataset
num_elements = 1000000
dataset = random.sample(range(1, 10000000), num_elements)

# Insert dataset into AVL tree and count rotations
avl_tree = AVLTree()
for value in dataset:
    avl_tree.insert_key(value)

# Insert dataset into Red-Black tree and count rotations
rb_tree = RBTree()
for value in dataset:
    rb_tree.insert(value)

# Print the results
print(f"Total rotations in AVL Tree: {avl_tree.rotations}")
print(f"Total rotations in Red-Black Tree: {rb_tree.rotations}")

dataset = [5, 2, 9, 1, 3, 8, 10, 4, 7, 6]

avl_tree = AVLTree()
for value in dataset:
    avl_tree.insert_key(value)

# Insert dataset into Red-Black tree and count rotations
rb_tree = RBTree()
for value in dataset:
    rb_tree.insert(value)

# Print the results
print(f"Total rotations in AVL Tree: {avl_tree.rotations}")
print(f"Total rotations in Red-Black Tree: {rb_tree.rotations}")