# Dynamic Array Implementation

## Overview
A dynamic array (also known as a resizable array) that can grow and shrink in size during runtime.

## Implementation Features
- **Automatic resizing**: Doubles capacity when full
- **Memory efficient**: Shrinks when utilization is low
- **O(1) amortized insertion**: Fast append operations
- **Comprehensive error handling**: Proper bounds checking

## Time Complexities
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Access    | O(1)         | O(1)       |
| Search    | O(n)         | O(n)       |
| Insertion | O(1)*        | O(n)       |
| Deletion  | O(n)         | O(n)       |

*Amortized time complexity

## Usage Example
```python
# Create a new dynamic array
arr = DynamicArray()

# Add elements
arr.append(1)
arr.append(2)
arr.append(3)

# Access elements
print(arr[0])  # Output: 1

# Insert at specific position
arr.insert(1, 5)  # Insert 5 at index 1

# Delete elements
arr.delete(2)  # Delete element at index 2

# Get size
print(len(arr))  # Current number of elements
```

## Files
- `dynamic_array.py`: Main implementation
- `test_dynamic_array.py`: Unit tests (to be created)