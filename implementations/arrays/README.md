# Arrays Implementation 📊

This directory contains implementations of array-based data structures and algorithms.

## Files

### `dynamic_array.py`
Complete implementation of a dynamic array (similar to Python's `list`) with:
- **Automatic resizing**: Doubles capacity when full, halves when 1/4 full
- **Amortized O(1) append**: Efficient element addition
- **Standard operations**: Insert, delete, search, access
- **Memory optimization**: Shrinks to avoid wasted space

### Key Features
- Time complexity analysis for all operations
- Comprehensive error handling
- Memory-efficient growth strategy
- Ready-to-use for Day 1 problems

### Usage Example
```python
from dynamic_array import DynamicArray

# Create dynamic array
arr = DynamicArray()

# Add elements
for i in range(100):
    arr.append(i)  # O(1) amortized

# Access elements
first = arr[0]     # O(1)
last = arr[-1]     # Need to implement negative indexing

# Search for element
index = arr.find(50)  # O(n)

# Insert/delete
arr.insert(10, 999)   # O(n)
deleted = arr.delete(5)  # O(n)
```

## Time Complexities
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Access    | O(1)          | Direct indexing |
| Append    | O(1)*         | *Amortized, O(n) worst case |
| Insert    | O(n)          | Requires shifting elements |
| Delete    | O(n)          | Requires shifting elements |
| Search    | O(n)          | Linear scan |

## Space Complexity
- **Space**: O(n) where n is the number of elements
- **Extra space**: O(1) for operations (not counting resizing)

## Day 1 Connection
This implementation directly supports solving Day 1 problems:
- **Two Sum**: Use for storing and accessing elements
- **Remove Duplicates**: Demonstrates in-place operations
- **Rotate Array**: Shows array manipulation techniques
- **Contains Duplicate**: Supports search operations

## Next Steps
- [ ] Add iterator protocol support
- [ ] Implement negative indexing
- [ ] Add slice notation support
- [ ] Performance benchmarking vs Python list
- [ ] Add more comprehensive test cases