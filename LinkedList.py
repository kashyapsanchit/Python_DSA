from typing import Counter


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():                                     # A -> B -> C -> D -> 0
    def __init__(self) -> None:
        self.head = None

    def print(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def push(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Node not present in the list!")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def delete(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return 
        
        prev = None
        while cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            print("Node not present in the list")
            return

        prev.next = cur_node.next
        cur_node = None
        
    def delete_by_pos(self, pos):

        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return
        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            print("Node not found")
            return

        prev.next = cur_node.next
        cur_node = None



    def length(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count+=1
            cur_node = cur_node.next
        print(count)



    def node_swap(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head                                   # A -> B -> C -> D -> 0
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 and curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):

        curr_node = self.head
        prev = None

        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev
            prev = curr_node
            cur = nxt
        self.head = prev

        


ll = LinkedList()
ll.push("A")
ll.push("B")
ll.push("C")
ll.push("D")
# ll.prepend("T")
# ll.insert_after_node(ll.head.next, "L")
# ll.print()
# ll.reverse_iterative()
ll.node_swap("A", "D")

# ll.delete_by_pos(5)
# ll.length()
ll.print()

        