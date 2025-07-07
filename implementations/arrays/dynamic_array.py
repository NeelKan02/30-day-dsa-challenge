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
        pass
    
    def __len__(self):
        """Return the number of elements in the array."""
        # TODO: Return the current size
        pass
    
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
        pass
    
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
        pass
    
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
        pass
    
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
        pass
    
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
        pass
    
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
        pass
    
    def _should_shrink(self):
        """
        Check if array should be shrunk.
        
        Returns:
            bool: True if array should be shrunk
        """
        # TODO: Return True if size is less than 1/4 of capacity
        # TODO: Ensure minimum capacity of 1
        pass
    
    def is_empty(self):
        """Check if the array is empty."""
        # TODO: Return True if size is 0
        pass
    
    def capacity(self):
        """Return the current capacity of the array."""
        # TODO: Return current capacity
        pass
    
    def __str__(self):
        """String representation of the array."""
        # TODO: Return string representation of elements
        pass
    
    def __repr__(self):
        """Official string representation of the array."""
        # TODO: Return detailed representation
        pass


# Test the implementation (to be run during Day 1)
if __name__ == "__main__":
    # TODO: Add basic tests
    # Test 1: Create array and add elements
    # Test 2: Test resizing behavior
    # Test 3: Test insertion and deletion
    # Test 4: Test edge cases
    
    print("DynamicArray implementation template created!")
    print("Complete the TODO items during Day 1 study session.")