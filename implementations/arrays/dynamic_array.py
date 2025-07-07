"""
Dynamic Array Implementation
Author: NeelKan02
Date: July 7, 2025
Part of: 30-Day DSA Challenge - Day 1

A dynamic array (similar to Python's list) that automatically resizes
when capacity is exceeded. Demonstrates fundamental array operations
and amortized analysis concepts.
"""

class DynamicArray:
    """
    A dynamic array implementation that grows and shrinks as needed.
    
    Features:
    - Automatic resizing when capacity is exceeded
    - Amortized O(1) append operation
    - O(1) access and update operations
    - O(n) insertion and deletion with shifting
    """
    
    def __init__(self, initial_capacity=4):
        """
        Initialize the dynamic array.
        
        Args:
            initial_capacity (int): Initial capacity of the array (default: 4)
        """
        self._capacity = initial_capacity
        self._size = 0
        self._data = [None] * self._capacity
    
    def __len__(self):
        """Return the current size of the array."""
        return self._size
    
    def __getitem__(self, index):
        """
        Get element at the specified index.
        
        Args:
            index (int): The index to access
            
        Returns:
            The element at the specified index
            
        Raises:
            IndexError: If index is out of bounds
        """
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        return self._data[index]
    
    def __setitem__(self, index, value):
        """
        Set element at the specified index.
        
        Args:
            index (int): The index to update
            value: The new value to set
            
        Raises:
            IndexError: If index is out of bounds
        """
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        self._data[index] = value
    
    def append(self, item):
        """
        Add an element to the end of the array.
        Amortized O(1) time complexity.
        
        Args:
            item: The element to add
        """
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        
        self._data[self._size] = item
        self._size += 1
    
    def insert(self, index, item):
        """
        Insert an element at the specified index.
        O(n) time complexity due to shifting.
        
        Args:
            index (int): The index where to insert
            item: The element to insert
            
        Raises:
            IndexError: If index is out of bounds
        """
        if not 0 <= index <= self._size:
            raise IndexError(f"Index {index} out of bounds for insertion")
        
        if self._size >= self._capacity:
            self._resize(self._capacity * 2)
        
        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        
        self._data[index] = item
        self._size += 1
    
    def delete(self, index):
        """
        Remove element at the specified index.
        O(n) time complexity due to shifting.
        
        Args:
            index (int): The index of element to remove
            
        Returns:
            The removed element
            
        Raises:
            IndexError: If index is out of bounds
        """
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} out of bounds for size {self._size}")
        
        removed_item = self._data[index]
        
        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        
        self._size -= 1
        self._data[self._size] = None  # Clear the reference
        
        # Shrink if necessary (when size is 1/4 of capacity)
        if self._size <= self._capacity // 4 and self._capacity > 4:
            self._resize(self._capacity // 2)
        
        return removed_item
    
    def pop(self):
        """
        Remove and return the last element.
        Amortized O(1) time complexity.
        
        Returns:
            The last element
            
        Raises:
            IndexError: If array is empty
        """
        if self._size == 0:
            raise IndexError("Pop from empty array")
        
        return self.delete(self._size - 1)
    
    def get(self, index):
        """
        Get element at index (alternative to __getitem__).
        
        Args:
            index (int): The index to access
            
        Returns:
            The element at the specified index
        """
        return self[index]
    
    def set(self, index, value):
        """
        Set element at index (alternative to __setitem__).
        
        Args:
            index (int): The index to update
            value: The new value to set
        """
        self[index] = value
    
    def size(self):
        """Return the current number of elements."""
        return self._size
    
    def capacity(self):
        """Return the current capacity of the array."""
        return self._capacity
    
    def is_empty(self):
        """Return True if the array is empty."""
        return self._size == 0
    
    def _resize(self, new_capacity):
        """
        Resize the internal array to the new capacity.
        
        Args:
            new_capacity (int): The new capacity
        """
        old_data = self._data
        self._capacity = new_capacity
        self._data = [None] * self._capacity
        
        # Copy existing elements
        for i in range(self._size):
            self._data[i] = old_data[i]
    
    def __str__(self):
        """Return string representation of the array."""
        elements = [str(self._data[i]) for i in range(self._size)]
        return f"[{', '.join(elements)}]"
    
    def __repr__(self):
        """Return detailed representation of the array."""
        return f"DynamicArray(size={self._size}, capacity={self._capacity}, data={str(self)})"


# TODO: Add these methods for complete implementation
# def find(self, item):
#     """Find the index of the first occurrence of item."""
#     pass
#
# def remove(self, item):
#     """Remove the first occurrence of item."""
#     pass
#
# def extend(self, iterable):
#     """Extend the array with elements from iterable."""
#     pass


if __name__ == "__main__":
    # Basic testing - Run this to verify implementation
    print("Testing Dynamic Array Implementation")
    print("=" * 40)
    
    # Create array
    arr = DynamicArray()
    print(f"Initial array: {arr}")
    print(f"Size: {arr.size()}, Capacity: {arr.capacity()}")
    
    # Test append
    print("\nTesting append:")
    for i in range(5):
        arr.append(i * 10)
        print(f"Appended {i * 10}: {arr}")
    
    # Test access
    print(f"\nElement at index 2: {arr[2]}")
    
    # Test insertion
    print(f"\nInserting 25 at index 3:")
    arr.insert(3, 25)
    print(f"Array: {arr}")
    
    # Test deletion
    print(f"\nDeleting element at index 1:")
    removed = arr.delete(1)
    print(f"Removed: {removed}, Array: {arr}")
    
    print(f"\nFinal array: {arr}")
    print(f"Size: {arr.size()}, Capacity: {arr.capacity()}")