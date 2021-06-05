from typing import BinaryIO


class Node(object):
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self) -> None:
        self.root = None

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _find(self, data, cur_node):
        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        else:
            if data == cur_node.data:
                print("Element Found!!")
                return True
            else:
                return None

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _inorder_print(self, cur_node):
        if cur_node:
            self._inorder_print(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print(cur_node.right)

    def inorder_print(self):
        if self.root:
            self._inorder_print(self.root)

    def _is_bst_satisfied(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self._is_bst_satisfied(cur_node.left, cur_node.left.data)
            else:
                return False
        
        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst_satisfied(cur_node.right, cur_node.right.data)
            else:
                return False



    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)
            if is_satisfied is None:
                return True
            return False

        return True

        
tree = BST()
tree.insert(5)
tree.insert(2)
tree.insert(8)
tree.insert(7)
tree.insert(1)
tree.insert(3)

print(tree.is_bst_satisfied())
# print(tree.find(10))
# print(tree.inorder_print())
