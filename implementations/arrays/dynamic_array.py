"""
Dynamic Array Implementation for 30-Day DSA Challenge
Author: NeelKan02
Date: July 7, 2025 (Day 1)

A dynamic array (like Python's list) that automatically resizes
when capacity is exceeded. This implementation focuses on:
- Automatic resizing with amortized O(1) append
- Basic array operations with optimal time complexity
- Memory-efficient growth strategy
"""

class DynamicArray:
    """
    Dynamic Array implementation with automatic resizing.
    
    Time Complexities:
    - Access (get/set): O(1)
    - Append: O(1) amortized, O(n) worst case
    - Insert: O(n)
    - Delete: O(n)
    - Search: O(n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self, initial_capacity=8):
        """Initialize dynamic array with given initial capacity."""
        self._capacity = max(initial_capacity, 1)
        self._size = 0
        self._data = [None] * self._capacity
    
    def __len__(self):
        """Return the number of elements in the array."""
        return self._size
    
    def __getitem__(self, index):
        """Get element at given index."""
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} out of range")
        return self._data[index]
    
    def __setitem__(self, index, value):
        """Set element at given index."""
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} out of range")
        self._data[index] = value
    
    def __str__(self):
        """String representation of the array."""
        elements = [str(self._data[i]) for i in range(self._size)]
        return f"DynamicArray([{', '.join(elements)}])"
    
    def __repr__(self):
        """Developer representation of the array."""
        return f"DynamicArray(size={self._size}, capacity={self._capacity})"
    
    def capacity(self):
        """Return current capacity of the array."""
        return self._capacity
    
    def is_empty(self):
        """Check if array is empty."""
        return self._size == 0
    
    def _resize(self, new_capacity):
        """
        Resize the internal array to new capacity.
        
        Args:
            new_capacity (int): New capacity for the array
        """
        old_data = self._data
        self._capacity = new_capacity
        self._data = [None] * self._capacity
        
        # Copy existing elements
        for i in range(self._size):
            self._data[i] = old_data[i]
    
    def append(self, value):
        """
        Add element to the end of array.
        
        Args:
            value: Element to add
            
        Time Complexity: O(1) amortized
        """
        # Resize if necessary (double the capacity)
        if self._size >= self._capacity:
            self._resize(2 * self._capacity)
        
        self._data[self._size] = value
        self._size += 1
    
    def insert(self, index, value):
        """
        Insert element at given index.
        
        Args:
            index (int): Position to insert at
            value: Element to insert
            
        Time Complexity: O(n)
        """
        if not 0 <= index <= self._size:
            raise IndexError(f"Index {index} out of range")
        
        # Resize if necessary
        if self._size >= self._capacity:
            self._resize(2 * self._capacity)
        
        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        
        self._data[index] = value
        self._size += 1
    
    def delete(self, index):
        """
        Delete element at given index.
        
        Args:
            index (int): Position to delete from
            
        Returns:
            Deleted element
            
        Time Complexity: O(n)
        """
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} out of range")
        
        deleted_value = self._data[index]
        
        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        
        self._size -= 1
        self._data[self._size] = None  # Clear reference
        
        # Shrink if array is 1/4 full (to avoid thrashing)
        if self._size > 0 and self._size <= self._capacity // 4:
            self._resize(self._capacity // 2)
        
        return deleted_value
    
    def pop(self):
        """
        Remove and return last element.
        
        Returns:
            Last element
            
        Time Complexity: O(1) amortized
        """
        if self.is_empty():
            raise IndexError("pop from empty array")
        
        return self.delete(self._size - 1)
    
    def find(self, value):
        """
        Find first occurrence of value.
        
        Args:
            value: Element to search for
            
        Returns:
            Index of first occurrence, -1 if not found
            
        Time Complexity: O(n)
        """
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1
    
    def clear(self):
        """Clear all elements from array."""
        self._size = 0
        for i in range(self._capacity):
            self._data[i] = None


# TODO: Add comprehensive test cases
# TODO: Implement iterator protocol (__iter__, __next__)
# TODO: Add slice notation support
# TODO: Benchmark against Python's built-in list

if __name__ == "__main__":
    # Basic testing
    arr = DynamicArray()
    
    # Test append
    for i in range(10):
        arr.append(i)
    print(f"After appending 0-9: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.capacity()}")
    
    # Test insert
    arr.insert(0, -1)
    print(f"After inserting -1 at index 0: {arr}")
    
    # Test delete
    deleted = arr.delete(5)
    print(f"Deleted element at index 5: {deleted}")
    print(f"Array after deletion: {arr}")
    
    # Test find
    index = arr.find(7)
    print(f"Index of element 7: {index}")
    
    print(f"\nFinal array: {arr}")
    print(f"Representation: {repr(arr)}")