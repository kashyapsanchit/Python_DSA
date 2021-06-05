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


        
tree = BST()
tree.insert(5)
tree.insert(2)
tree.insert(8)
tree.insert(7)
tree.insert(1)
tree.insert(3)

print(tree.find(10))
