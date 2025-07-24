class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        if self.head == None:
            return True
        
        return False
    
    def length(self):
        iter = self.head
        count = 0
        while iter:
            count += 1
            iter = iter.next

        return count
    
    def display(self):
        if self.head is None:
            return "Empty list"
        
        result = []
        iter = self.head
        while iter:
            result.append(str(iter.data))
            iter = iter.next
        
        return " -> ".join(result)

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        self.size += 1

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        iter = self.head
        while iter.next:
            iter = iter.next
        
        iter.next = Node(data, None)
        self.size += 1

    def insert_at_position(self, data, pos):
        if pos > self.size:
            raise IndexError (f"{pos} is incorrect for list of size{self.size}")

        iter = self.head
        while pos:
            iter = iter.next
            pos -= 1

        node = Node(data, iter.next)
        iter.next = node
        self.size += 1

    def insert_after_value(self, data, val):
        iter = self.head
        while iter.next.data != val:
            iter = iter.next

        node = Node(data, iter.next)
        iter.next = node
        self.size += 1
    
    def delete_at_beginning(self):
        if self.head is None:
            raise ValueError("List is empty!")
        
        self.head = self.head.next   
        self.size -= 1

    def delete_at_end(self):
        if self.head is None:
            return f"List is empty!!"
        
        iter = self.head
        while iter.next.next:
            iter = iter.next

        iter.next = None
        self.size -= 1

    def delete_at_position(self, pos):
        if pos > self.size:
            raise IndexError (f"{pos} is invalid for list of size {self.size}")
        
        iter = self.head
        while pos > 0:
            iter = iter.next
            pos -= 1

        iter.next = iter.next.next
        self.size -= 1

    def delete_by_value(self, data):
        iter = self.head
        while iter.next.data != data:
            iter = iter.next

        iter.next = iter .next.next 
        self.size -= 1

    def search(self, data):
        if self.is_empty():
            return -1
        
        pos = 0
        iter = self.head
        while iter:
            if iter.data == data:
                return pos
            iter = iter.next
            pos += 1

        return pos
    
    def get_at_position(self, position):
        if self.is_empty():
            raise ValueError("List is empty!")
        
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is invalid for list of size {self.size}")
        
        iter = self.head
        for _ in range(position):
            iter = iter.next

        return iter.data
    
    def contains(self, data):
        iter = self.head
        while iter:  # Check all nodes including last
            if iter.data == data:
                return True
            iter = iter.next
        return False
    
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node

        self.head = prev

    def clear(self):
        self.head = None

    def remove_duplicates(self):
        if self.is_empty():
            return
        
        seen = set()
        current = self.head
        prev = None
        
        while current:
            if current.data in seen:
                # Remove duplicate node
                prev.next = current.next
                self.size -= 1
            else:
                # First occurrence, add to seen set
                seen.add(current.data)
                prev = current
            
            current = current.next

    def get_middle(self):
        if self.is_empty():
            raise ValueError("List is empty!")
   
        slow = self.head
        fast = self.head
        
        # Check both fast and fast.next to avoid null pointer
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow.data