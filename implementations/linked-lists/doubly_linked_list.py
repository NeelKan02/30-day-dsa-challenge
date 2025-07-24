class DoublyNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Important: track both head and tail
        self.size = 0

    def is_empty(self):
        return True if self.size == 0 else False
    
    def length(self):
        return self.size
    
    def display_forward(self):
        if self.size == 0:
            return f"List is empty!!"
        
        result = []
        iter = self.head
        while iter:
            result.append(str(iter.data))
            iter = iter.next

        return " <-> ".join(result)
    
    def display_backward(self):
        if self.size == 0:
            return f"List is empty!!"
        
        result = []
        iter = self.tail
        while iter:
            result.append(str(iter.data))
            iter = iter.prev

        return " <-> ".join(result)
    
    def insert_at_beginning(self, data):
        """Insert node at the start - O(1)"""
        node = DoublyNode(data)
        
        if self.size == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        self.size += 1

        
    def insert_at_end(self, data):
        """Insert node at the end - O(1)"""
        if self.size == 0:
            self.insert_at_beginning(data)
            return
        
        node = DoublyNode(data, None, self.tail)
        self.tail.next = node  # Critical: link old tail to new node
        self.tail = node
        self.size += 1
        
    def insert_at_position(self, data, position):
        """Insert node at specific position - O(n)"""
        if position < 0 or position > self.size:
            raise IndexError(f"Position {position} is not valid for list of size {self.size}")
        
        if position == 0:  # 0-based indexing
            self.insert_at_beginning(data)
            return
        
        if position == self.size:
            self.insert_at_end(data)
            return
        
        # Find the position
        current = self.head
        for _ in range(position):
            current = current.next
        
        # Create new node and update pointers
        node = DoublyNode(data, current, current.prev)
        current.prev.next = node
        current.prev = node
        self.size += 1

    def insert_after_value(self, data_after, data_to_insert):
        """Insert after a specific value"""
        if self.is_empty():
            raise ValueError("List is empty!")
        
        current = self.head
        while current and current.data != data_after:
            current = current.next
        
        if not current:
            raise ValueError(f"Value {data_after} not found")
        
        node = DoublyNode(data_to_insert, current.next, current)
        
        if current.next:  # Not inserting at end
            current.next.prev = node
        else:  # Inserting at end
            self.tail = node
        
        current.next = node
        self.size += 1
        
    def insert_before_value(self, data_before, data_to_insert):
        """Insert before a specific value"""
        if self.is_empty():
            raise ValueError("List is empty!")
        
        current = self.head
        while current and current.data != data_before:
            current = current.next
        
        if not current:
            raise ValueError(f"Value {data_before} not found")
        
        node = DoublyNode(data_to_insert, current, current.prev)
        
        if current.prev:  # Not inserting at beginning
            current.prev.next = node
        else:  # Inserting at beginning
            self.head = node
        
        current.prev = node
        self.size += 1

    def delete_at_beginning(self):
        """Delete first node - O(1)"""
        if self.is_empty():
            raise ValueError("List is empty!!")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        
    def delete_at_end(self):
        """Delete last node - O(1) (advantage over singly!)"""
        if self.is_empty():
            raise ValueError("List is empty!!")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        
    def delete_at_position(self, position):
        """Delete node at specific position - O(n)"""
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is invalid for list of size {self.size}")
        if position == 0:
            self.delete_at_beginning()
            return
        if position == self.size - 1:
            self.delete_at_end()
            return
        current = self.head
        for _ in range(position):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        
    def delete_by_value(self, data):
        """Delete first occurrence of value - O(n)"""
        if self.is_empty():
            raise ValueError("List is empty!!")
        
        current = self.head
        while current and current.data != data:
            current = current.next
        
        if not current:
            raise ValueError(f"Value {data} not found!!")
        
        # Handle different cases
        if current == self.head and current == self.tail:
            # Only one node
            self.head = self.tail = None
        elif current == self.head:
            # First node
            self.head = current.next
            self.head.prev = None
        elif current == self.tail:
            # Last node
            self.tail = current.prev
            self.tail.next = None
        else:
            # Middle node
            current.prev.next = current.next
            current.next.prev = current.prev
        
        self.size -= 1
        
    def delete_all_occurrences(self, data):
        """Delete all nodes with given value"""
        if self.is_empty():
            raise ValueError("List is empty!!")
        
        current = self.head
        found = False
        
        while current:
            if current.data == data:
                found = True
                next_node = current.next  # Save next before deletion
                
                if current == self.head and current == self.tail:
                    # Only one node
                    self.head = self.tail = None
                elif current == self.head:
                    # First node
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    # Last node
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    # Middle node
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                self.size -= 1
                current = next_node  # Move to saved next node
            else:
                current = current.next
        
        if not found:
            raise ValueError(f"Value {data} not found")

    def search(self, data):
        """Search for a value, return position or -1"""
        if self.is_empty():
            return -1
        
        position = 0
        current = self.head
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        
        return -1  # Not found
        
    def search_from_end(self, data):
        """Search backwards from tail (unique advantage)"""
        if self.is_empty():
            return -1

        position = self.size-1
        current = self.tail
        while current:
            if current.data == data:
                return position
            current = current.prev
            position -= 1

        return -1
    
    def get_at_position(self, position):
        """Get value at specific position"""
        if self.is_empty():
            raise ValueError("List is empty!!")
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is invalid for list of size {self.size}")
        current = self.head
        for _ in range(position):
            current = current.next
        return current.data
        
    def contains(self, data):
        """Check if value exists in list"""
        if self.is_empty():
            return False

        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next

        return False
    
    def reverse(self):
        """Reverse the doubly linked list"""
        if self.is_empty():
            return
                
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head
        return        
        
    def get_middle(self):
        """Find middle element using slow/fast pointers"""
        if self.is_empty():
            return None

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
        
    def remove_duplicates(self):
        """Remove duplicate values"""
        if self.is_empty():
            return 
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                next_node = current.next

                if current == self.head and current == self.tail:
                    self.head = self.tail = None
                elif current == self.head:
                # First node
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                # Last node
                    self.tail = current.prev
                    self.tail.next = None
                else:
                # Middle node
                    current.prev.next = current.next
                    current.next.prev = current.prev
        
                self.size -= 1
                current = next_node
            else:
                seen.add(current.data)
                current = current.next

    def clear(self):
        """Remove all nodes"""
        self.head = self.tail = None
        self.size = 0
        
    def clone(self):
        """Create a deep copy of the list"""
        new_list = DoublyLinkedList()

        current = self.head
        while current:
            new_list.insert_at_end(current.data)
            current = current.next

        return new_list
    

if __name__ == "__main__":
    DL = DoublyLinkedList()
    print(DL.is_empty())
    DL.insert_at_beginning(1)
    DL.insert_at_beginning(2)
    DL.insert_at_end(3)
    DL.insert_at_position(4,2)
    DL.insert_at_position(5,1)
    DL.insert_after_value(1,6)
    DL.insert_before_value(6,7)
    print(DL.display_forward())
    print(DL.display_backward())
    print(DL.length())
    DL.delete_at_position(3)
    DL.delete_at_beginning()
    DL.delete_at_end()
    print(DL.get_middle())
    print(DL.is_empty())
    print(DL.search(1))
    print(DL.display_forward())
    

