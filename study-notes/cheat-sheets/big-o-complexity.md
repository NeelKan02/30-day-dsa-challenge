# 📊 Big O Complexity Cheat Sheet

**Quick reference for algorithm and data structure complexities**

---

## 🕐 Time Complexity Classes

| Notation | Name | Example | Description |
|----------|------|---------|-------------|
| O(1) | Constant | Array access | Same time regardless of input size |
| O(log n) | Logarithmic | Binary search | Time grows logarithmically with input |
| O(n) | Linear | Array traversal | Time grows linearly with input |
| O(n log n) | Linearithmic | Merge sort | Efficient sorting algorithms |
| O(n²) | Quadratic | Bubble sort | Nested loops over input |
| O(n³) | Cubic | Triple nested loops | Three nested loops |
| O(2ⁿ) | Exponential | Fibonacci (naive) | Doubles with each input increase |
| O(n!) | Factorial | Traveling salesman | Permutation of all elements |

### 📈 Growth Rate Comparison
```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)
```

---

## 📊 Data Structures Complexity

### Arrays / Lists
| Operation | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Access | O(1) | O(1) | O(1) | Index-based access |
| Search | O(1) | O(n) | O(n) | Unsorted array |
| Insertion | O(1) | O(n) | O(n) | At end vs middle |
| Deletion | O(1) | O(n) | O(n) | At end vs middle |

### Dynamic Arrays (Python Lists)
| Operation | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Access | O(1) | O(1) | O(1) | Index-based |
| Append | O(1) | O(1) | O(n) | Amortized O(1) |
| Insert | O(n) | O(n) | O(n) | Shifting required |
| Delete | O(n) | O(n) | O(n) | Shifting required |

### Linked Lists
| Operation | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Access | O(1) | O(n) | O(n) | Head access vs search |
| Search | O(1) | O(n) | O(n) | Must traverse |
| Insertion | O(1) | O(1) | O(1) | With reference |
| Deletion | O(1) | O(1) | O(1) | With reference |

### Hash Tables (Dictionaries)
| Operation | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Access | O(1) | O(1) | O(n) | Good hash function |
| Search | O(1) | O(1) | O(n) | Good hash function |
| Insertion | O(1) | O(1) | O(n) | Good hash function |
| Deletion | O(1) | O(1) | O(n) | Good hash function |

### Stacks & Queues
| Operation | Time | Notes |
|-----------|------|-------|
| Push/Enqueue | O(1) | Add to top/end |
| Pop/Dequeue | O(1) | Remove from top/front |
| Peek/Front | O(1) | View without removing |
| Search | O(n) | Must check all elements |

### Binary Search Trees (Balanced)
| Operation | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Access | O(log n) | O(log n) | O(n) | Worst = unbalanced |
| Search | O(log n) | O(log n) | O(n) | Worst = unbalanced |
| Insertion | O(log n) | O(log n) | O(n) | Worst = unbalanced |
| Deletion | O(log n) | O(log n) | O(n) | Worst = unbalanced |

### Heaps (Binary Heap)
| Operation | Time | Notes |
|-----------|------|-------|
| Get Min/Max | O(1) | Root element |
| Insert | O(log n) | Bubble up |
| Delete Min/Max | O(log n) | Bubble down |
| Build Heap | O(n) | From array |

### Graphs (V = vertices, E = edges)
| Operation | Adjacency List | Adjacency Matrix |
|-----------|----------------|------------------|
| Add Vertex | O(1) | O(V²) |
| Add Edge | O(1) | O(1) |
| Remove Vertex | O(V + E) | O(V²) |
| Remove Edge | O(E) | O(1) |
| Query Edge | O(V) | O(1) |

---

## 🔍 Algorithm Complexities

### Sorting Algorithms
| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |

### Searching Algorithms
| Algorithm | Best | Average | Worst | Notes |
|-----------|------|---------|-------|-------|
| Linear Search | O(1) | O(n) | O(n) | Unsorted data |
| Binary Search | O(1) | O(log n) | O(log n) | Sorted data |
| BFS | O(V + E) | O(V + E) | O(V + E) | Graph traversal |
| DFS | O(V + E) | O(V + E) | O(V + E) | Graph traversal |

---

## 💾 Space Complexity

### Space Types
- **Input Space**: Space used by input data
- **Auxiliary Space**: Extra space used by algorithm
- **Total Space**: Input + Auxiliary space

### Common Space Complexities
| Complexity | Description | Example |
|------------|-------------|---------|
| O(1) | Constant extra space | In-place algorithms |
| O(log n) | Logarithmic space | Recursive algorithms |
| O(n) | Linear space | Creating copy of input |
| O(n²) | Quadratic space | 2D arrays |

---

## 🎯 Quick Rules for Analysis

### Time Complexity Rules
1. **Drop constants**: O(2n) → O(n)
2. **Drop lower terms**: O(n² + n) → O(n²)
3. **Different inputs use different variables**: O(a + b), not O(n)
4. **Nested loops multiply**: Two nested loops = O(n²)
5. **Sequential loops add**: Two separate loops = O(n + m)

### Space Complexity Rules
1. **Variables**: O(1) space each
2. **Arrays**: O(n) space for n elements
3. **Recursion**: O(depth) for call stack
4. **Hash tables**: O(n) for n key-value pairs

---

## 🚀 Optimization Tips

### When to Optimize
1. **Premature optimization is evil** - Get it working first
2. **Measure before optimizing** - Profile to find bottlenecks
3. **Big O matters most** - O(n²) → O(n log n) > O(n log n) → O(n)

### Common Optimization Techniques
1. **Hash tables** - O(n) lookup instead of O(n²) nested loops
2. **Two pointers** - O(n) instead of O(n²) for array problems
3. **Sliding window** - O(n) for subarray problems
4. **Binary search** - O(log n) instead of O(n) for sorted data
5. **Dynamic programming** - Avoid recalculating subproblems

---

## 📱 Mobile Quick Reference

### Must Remember O() Classes
```
O(1) - Constant      [Best]
O(log n) - Log       [Great]
O(n) - Linear        [Good]
O(n log n) - N Log N [Acceptable]
O(n²) - Quadratic    [Slow]
O(2ⁿ) - Exponential  [Avoid]
```

### Common Patterns
- **Nested loops** = O(n²)
- **Divide & conquer** = O(n log n)
- **Hash lookup** = O(1)
- **Tree operations** = O(log n)

---

**📝 Note**: These are typical complexities. Actual performance may vary based on implementation details, input characteristics, and system constraints.

**Last Updated**: July 7, 2025  
**Part of**: 30-Day DSA Challenge