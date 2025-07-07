# Big O Complexity Cheat Sheet 📊

A comprehensive reference for time and space complexity analysis during the 30-day DSA challenge.

## 🎯 Big O Notation Hierarchy

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
Best ←————————————————————————————————————————————————————————→ Worst
```

## 📈 Growth Rates Comparison

| n | O(1) | O(log n) | O(n) | O(n log n) | O(n²) | O(2ⁿ) |
|---|------|----------|------|------------|-------|-------|
| 1 | 1 | 1 | 1 | 1 | 1 | 2 |
| 10 | 1 | 3 | 10 | 33 | 100 | 1,024 |
| 100 | 1 | 7 | 100 | 664 | 10,000 | 1.27e30 |
| 1,000 | 1 | 10 | 1,000 | 9,966 | 1,000,000 | ∞ |

## 🏗️ Data Structure Operations

### Arrays
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Access | O(1) | O(1) | O(1) | O(n) |
| Search | O(1) | O(n) | O(n) | O(1) |
| Insert | O(1) | O(n) | O(n) | O(1) |
| Delete | O(1) | O(n) | O(n) | O(1) |

### Dynamic Array (e.g., Python list)
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Access | O(1) | O(1) | O(1) | O(n) |
| Search | O(1) | O(n) | O(n) | O(1) |
| Append | O(1) | O(1) | O(n) | O(1) |
| Insert | O(1) | O(n) | O(n) | O(1) |
| Delete | O(1) | O(n) | O(n) | O(1) |

### Linked List
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Access | O(1) | O(n) | O(n) | O(n) |
| Search | O(1) | O(n) | O(n) | O(1) |
| Insert | O(1) | O(1) | O(1) | O(1) |
| Delete | O(1) | O(1) | O(1) | O(1) |

### Stack
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Push | O(1) | O(1) | O(1) | O(n) |
| Pop | O(1) | O(1) | O(1) | O(1) |
| Peek | O(1) | O(1) | O(1) | O(1) |
| Search | O(1) | O(n) | O(n) | O(1) |

### Queue
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Enqueue | O(1) | O(1) | O(1) | O(n) |
| Dequeue | O(1) | O(1) | O(1) | O(1) |
| Front | O(1) | O(1) | O(1) | O(1) |
| Search | O(1) | O(n) | O(n) | O(1) |

### Hash Table
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Access | N/A | N/A | N/A | O(n) |
| Search | O(1) | O(1) | O(n) | O(1) |
| Insert | O(1) | O(1) | O(n) | O(1) |
| Delete | O(1) | O(1) | O(n) | O(1) |

### Binary Search Tree
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Access | O(log n) | O(log n) | O(n) | O(n) |
| Search | O(log n) | O(log n) | O(n) | O(1) |
| Insert | O(log n) | O(log n) | O(n) | O(1) |
| Delete | O(log n) | O(log n) | O(n) | O(1) |

### Heap (Binary)
| Operation | Best | Average | Worst | Space |
|-----------|------|---------|-------|-------|
| Find Min/Max | O(1) | O(1) | O(1) | O(n) |
| Insert | O(1) | O(log n) | O(log n) | O(1) |
| Delete Min/Max | O(log n) | O(log n) | O(log n) | O(1) |
| Build Heap | O(n) | O(n) | O(n) | O(1) |

## 🔄 Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Simple, inefficient |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No | Always O(n²) |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes | Good for small arrays |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide and conquer |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Average case optimal |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes | For integer ranges |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n + k) | Yes | For fixed-width integers |

## 🔍 Search Algorithms

| Algorithm | Best | Average | Worst | Space | Notes |
|-----------|------|---------|-------|-------|-------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) | Works on unsorted data |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) | Requires sorted data |
| **DFS** | O(1) | O(V + E) | O(V + E) | O(V) | Graph traversal |
| **BFS** | O(1) | O(V + E) | O(V + E) | O(V) | Graph traversal |

## 🧮 Common Complexity Patterns

### Linear Patterns O(n)
- Single loop through array
- Linear search
- Finding min/max in unsorted array

```python
# O(n) - Single pass
for i in range(n):
    print(arr[i])
```

### Logarithmic Patterns O(log n)
- Binary search on sorted array
- Tree operations (balanced)
- Divide and conquer (halveing)

```python
# O(log n) - Binary search
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### Quadratic Patterns O(n²)
- Nested loops
- Bubble sort, selection sort
- Comparing all pairs

```python
# O(n²) - Nested loops
for i in range(n):
    for j in range(n):
        print(arr[i], arr[j])
```

### Linearithmic Patterns O(n log n)
- Efficient sorting (merge, heap, quick)
- Divide and conquer with linear work

```python
# O(n log n) - Merge sort pattern
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # O(log n) levels
    right = merge_sort(arr[mid:])   # O(log n) levels
    
    return merge(left, right)       # O(n) work per level
```

## 🎯 Space Complexity Quick Reference

### O(1) - Constant Space
- Few variables regardless of input size
- In-place algorithms
- Iterative solutions with fixed variables

### O(log n) - Logarithmic Space
- Recursive call stack for divide and conquer
- Binary search recursion
- Balanced tree traversal

### O(n) - Linear Space
- Extra array of input size
- Hash table for frequency counting
- Queue/stack for BFS/DFS

### O(n²) - Quadratic Space
- 2D array/matrix of size n×n
- Adjacency matrix for graphs
- Dynamic programming tables

## 🚨 Common Analysis Mistakes

### ❌ Don't Do
- Assume nested loops always mean O(n²)
- Ignore the best case scenario
- Forget about space complexity
- Mix up average and worst case

### ✅ Do Remember
- Inner loop may not always run n times
- Amortized analysis for dynamic structures
- Space complexity includes call stack
- Consider all cases: best, average, worst

## 💡 Analysis Tips

1. **Count Operations**: Focus on the most expensive operation
2. **Ignore Constants**: O(2n) = O(n), O(n + 100) = O(n)
3. **Drop Lower Terms**: O(n² + n) = O(n²)
4. **Consider Input Size**: What grows as n increases?
5. **Worst Case Focus**: Usually most important for interviews

## 🎨 Complexity Visualization

```
Time Complexity Visual Guide:

O(1)     ▁         Constant - stays flat
O(log n) ▁▂▃       Logarithmic - slow growth
O(n)     ▁▂▃▄▅     Linear - steady growth
O(n²)    ▁▂▃▄▅▆▇█  Quadratic - rapid growth
O(2ⁿ)    ▁▂▃▄▅▆▇█▉ Exponential - explosive growth
```

## 🎯 Quick Decision Tree

**Need O(1) access?** → Array/Hash Table  
**Need O(log n) search?** → Binary Search Tree  
**Need O(1) insert/delete?** → Linked List/Hash Table  
**Need sorted order?** → BST or sorted array  
**Need LIFO?** → Stack  
**Need FIFO?** → Queue  
**Need priority ordering?** → Heap  

---
*Keep this cheat sheet handy during problem solving!* 📚