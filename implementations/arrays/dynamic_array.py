"""
Dynamic Array Implementation
A resizable array that grows and shrinks automatically.

Author: NeelKan02
Date: July 7, 2025
Part of: 30-Day DSA Challenge - Day 1
"""

class DynamicArray:
    """
    A dynamic array implementation that automatically resizes.
    
    Features:
    - Automatic resizing when capacity is exceeded
    - O(1) amortized insertion
    - Memory efficient with shrinking capability
    """
    
    def __init__(self, capacity=1):
        """
        Initialize the dynamic array.
        
        Args:
            capacity (int): Initial capacity of the array
        """
        # TODO: Initialize array with given capacity
        # TODO: Set size to 0 (number of elements)
        # TODO: Set capacity (total space available)

        self._capacity = capacity
        self.size = 0
        self.data = [None] * self._capacity
    
    def __len__(self):
        """Return the number of elements in the array."""
        # TODO: Return the current size
        
        return self.size
    
    def __getitem__(self, index):
        """
        Get element at given index.
        
        Args:
            index (int): Index of the element to retrieve
            
        Returns:
            The element at the given index
            
        Raises:
            IndexError: If index is out of bounds
        """
        # TODO: Check bounds
        # TODO: Return element at index
        
        if self.size == 0:
            raise IndexError(f"Cannot fetch values from empty array!!")
        
        if index < 0 or index >= self.size:
            raise IndexError(f"Index value entered {index} is out of bounds for array of size {self.size}")
        
        return self.data[index]            
    
    def __setitem__(self, index, value):
        """
        Set element at given index.
        
        Args:
            index (int): Index where to set the value
            value: Value to set
            
        Raises:
            IndexError: If index is out of bounds
        """
        # TODO: Check bounds
        # TODO: Set element at index
               
        if index < 0 or index >= self.size:
            raise IndexError(f"Index value {index} cannot be used for an array of size {self.size}")
        
        self.data[index] = value


    
    def append(self, value):
        """
        Add an element to the end of the array.
        
        Args:
            value: Element to add
            
        Time Complexity: O(1) amortized
        """
        # TODO: Check if resize is needed
        # TODO: Add element at the end
        # TODO: Increment size
        
        if self.size == self._capacity:
            self._resize(2*self._capacity)

        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """
        Insert an element at the given index.
        
        Args:
            index (int): Index where to insert
            value: Element to insert
            
        Time Complexity: O(n)
        
        Raises:
            IndexError: If index is out of bounds
        """
        # TODO: Check bounds (0 <= index <= size)
        # TODO: Check if resize is needed
        # TODO: Shift elements to the right
        # TODO: Insert element at index
        # TODO: Increment size
        if index <0 or index > self.size:
            raise IndexError (f"Index value {index} is wrong for array of size {self.size}.")
        
        if self.size == self._capacity:
            self._resize(2 * self._capacity)
        
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.size += 1
    
    def delete(self, index):
        """
        Delete element at the given index.
        
        Args:
            index (int): Index of element to delete
            
        Returns:
            The deleted element
            
        Time Complexity: O(n)
        
        Raises:
            IndexError: If index is out of bounds
        """
        # TODO: Check bounds
        # TODO: Store element to return
        # TODO: Shift elements to the left
        # TODO: Decrement size
        # TODO: Consider shrinking if utilization is low
        # TODO: Return deleted element
        
        if index < 0 or index >= self.size:
            raise IndexError (f"Array of size {self.size} does not have index {index}.")
        
        ele = self.data[index]

        for i in range(index,self.size-1):
            self.data[i] = self.data[i+1]

        self.size -= 1

        if self._should_shrink():
            self._resize(self._capacity//2)

        return ele
    
    def _resize(self, new_capacity):
        """
        Resize the internal array to new capacity.
        
        Args:
            new_capacity (int): New capacity for the array
            
        Time Complexity: O(n)
        """
        # TODO: Create new array with new capacity
        # TODO: Copy existing elements
        # TODO: Update capacity
        
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data = new_data
        self._capacity = new_capacity

    
    def _should_shrink(self):
        """
        Check if array should be shrunk.
        
        Returns:
            bool: True if array should be shrunk
        """
        # TODO: Return True if size is less than 1/4 of capacity
        # TODO: Ensure minimum capacity of 1
        return self.size < (self._capacity // 4) and self._capacity > 1
    
    def is_empty(self):
        """Check if the array is empty."""
        # TODO: Return True if size is 0
        return self.size == 0
    
    def capacity(self):
        """Return the current capacity of the array."""
        # TODO: Return current capacity
        return self._capacity
    
    def __str__(self):
        """String representation of the array."""
        # TODO: Return string representation of elements
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"

    
    def __repr__(self):
        """Official string representation of the array."""
        # TODO: Return detailed representation
        return f"DynamicArray(capacity={self._capacity}, size={self.size}, elements={self.__str__()})"


# Test the implementation (to be run during Day 1)
if __name__ == "__main__":
    # TODO: Add basic tests
    # Test 1: Create array and add elements
    # Test 2: Test resizing behavior
    # Test 3: Test insertion and deletion
    # Test 4: Test edge cases
    ar = DynamicArray(1)
    ar.append(4)
    ar.append(10)
    ar.append(1)
    ar.append(92)

    ar[2] = 3
    print(ar)
    ar
    ar.insert(4, 72)
    ar.insert(0, 8)
    print(ar)
    ar.delete(0)
    ar.delete(0)
    ar.delete(1)
    print(repr(ar))
    print("DynamicArray implementation template created!")
    print("Complete the TODO items during Day 1 study session.")