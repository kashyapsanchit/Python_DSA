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
        count = 1

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
    
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):

        curr_node = self.head
        prev = None

        while curr_node:
            nxt = curr_node.next
            curr_node.next = prev                           #A -> B -> C -> D -> 0 
                                                            #A <- B <- C <- D <- 0
            self.print_helper(curr_node, "CURR")
            self.print_helper(nxt, "NXT")
            self.print_helper(prev, "PREV")

            prev = curr_node
            curr_node = nxt
        self.head = prev

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
                
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_vals = dict()

        while cur:
            if cur.data in dup_vals:
                prev.next = cur.next
                cur = None                    # 1 -> 2 -> 6 -> 2 -> 5 -> 6 -> 0
            else:                             # 1 -> 2 -> 6 -> 5 -> 0
                dup_vals[cur.data] = 1
                prev = cur
            cur = prev.next


    def nth_to_last(self, n):

        cur = self.head
        count = 1
        while cur and count != n:
            cur = cur.next
            count += 1 
        
        if cur is None:
            return
        
        print(cur.data)
        return cur.data

    def count_occurunces(self, data):
        cur = self.head
        count = 0

        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        print(count)
        return count

ll = LinkedList()
ll.push("1")
ll.push("2")
ll.push("3")
ll.push("1")
ll.push("1")
ll.push("2")

ll.count_occurunces("2")
# ll.nth_to_last(6)
# ll.print()


# ll.prepend("T")
# ll.insert_after_node(ll.head.next, "L")
# ll.print()
# ll.reverse_iterative()
# ll.node_swap("A", "D")

# ll.delete_by_pos(5)
# ll.length()
# ll.print()

        