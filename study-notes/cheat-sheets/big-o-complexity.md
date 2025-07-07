# 📊 Big O Complexity Cheat Sheet

*Quick reference for algorithm analysis and complexity comparison*

---

## 🎯 Time Complexity Classes

### Common Big O Notations (Best to Worst)

| Notation | Name | Example Operations | Performance |
|----------|------|-------------------|-------------|
| **O(1)** | Constant | Array access, hash table lookup | ⚡ Excellent |
| **O(log n)** | Logarithmic | Binary search, balanced tree operations | 🚀 Great |
| **O(n)** | Linear | Array traversal, linear search | ✅ Good |
| **O(n log n)** | Linearithmic | Merge sort, heap sort, efficient sorting | 👍 Fair |
| **O(n²)** | Quadratic | Bubble sort, nested loops | ⚠️ Poor |
| **O(n³)** | Cubic | Triple nested loops | 🐌 Bad |
| **O(2ⁿ)** | Exponential | Recursive Fibonacci, subset generation | ❌ Terrible |
| **O(n!)** | Factorial | Permutation generation, traveling salesman | 💀 Abysmal |

### Visual Growth Comparison

```
For n = 10:
O(1):      1
O(log n):  3.32
O(n):      10
O(n log n): 33.2
O(n²):     100
O(2ⁿ):     1,024
O(n!):     3,628,800

For n = 100:
O(1):      1
O(log n):  6.64
O(n):      100
O(n log n): 664
O(n²):     10,000
O(2ⁿ):     1.27 × 10³⁰
O(n!):     9.33 × 10¹⁵⁷
```

---

## 📚 Data Structure Complexities

### Arrays & Lists

| Data Structure | Access | Search | Insertion | Deletion | Space |
|----------------|--------|--------|-----------|----------|-------|
| **Array** | O(1) | O(n) | O(n) | O(n) | O(n) |
| **Dynamic Array** | O(1) | O(n) | O(1)* | O(n) | O(n) |
| **Linked List** | O(n) | O(n) | O(1) | O(1) | O(n) |
| **Doubly Linked List** | O(n) | O(n) | O(1) | O(1) | O(n) |

*Amortized time complexity

### Stack & Queue

| Data Structure | Push/Enqueue | Pop/Dequeue | Peek | Space |
|----------------|--------------|-------------|------|-------|
| **Stack** | O(1) | O(1) | O(1) | O(n) |
| **Queue** | O(1) | O(1) | O(1) | O(n) |
| **Deque** | O(1) | O(1) | O(1) | O(n) |

### Hash-Based Structures

| Data Structure | Access | Search | Insertion | Deletion | Space |
|----------------|--------|--------|-----------|----------|-------|
| **Hash Table** | N/A | O(1)* | O(1)* | O(1)* | O(n) |
| **Hash Set** | N/A | O(1)* | O(1)* | O(1)* | O(n) |

*Average case; O(n) worst case

### Trees

| Data Structure | Access | Search | Insertion | Deletion | Space |
|----------------|--------|--------|-----------|----------|-------|
| **Binary Tree** | O(n) | O(n) | O(n) | O(n) | O(n) |
| **Binary Search Tree** | O(log n)* | O(log n)* | O(log n)* | O(log n)* | O(n) |
| **Balanced BST** | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| **Heap** | N/A | O(n) | O(log n) | O(log n) | O(n) |

*Average case; O(n) worst case for unbalanced BST

### Graphs

| Representation | Space | Add Vertex | Add Edge | Remove Vertex | Remove Edge | Query |
|----------------|-------|------------|----------|---------------|-------------|-------|
| **Adjacency List** | O(V + E) | O(1) | O(1) | O(V + E) | O(E) | O(V) |
| **Adjacency Matrix** | O(V²) | O(V²) | O(1) | O(V²) | O(1) | O(1) |

---

## 🔍 Algorithm Complexities

### Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable |
|-----------|-----------|--------------|------------|-------|--------|
| **Bubble Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| **Heap Sort** | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| **Counting Sort** | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes |
| **Radix Sort** | O(nk) | O(nk) | O(nk) | O(n + k) | Yes |

### Search Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) |
| **Hash Table Lookup** | O(1) | O(1) | O(n) | O(n) |

### Graph Algorithms

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| **DFS** | O(V + E) | O(V) |
| **BFS** | O(V + E) | O(V) |
| **Dijkstra's** | O((V + E) log V) | O(V) |
| **Bellman-Ford** | O(VE) | O(V) |
| **Floyd-Warshall** | O(V³) | O(V²) |
| **Kruskal's MST** | O(E log E) | O(V) |
| **Prim's MST** | O(E log V) | O(V) |

---

## 🎯 Analysis Guidelines

### Rules for Big O Analysis

1. **Drop Constants**: O(3n) → O(n)
2. **Drop Lower Terms**: O(n² + n) → O(n²)
3. **Different Inputs = Different Variables**: O(a + b) not O(n)
4. **Nested Loops**: Usually multiply complexities
5. **Sequential Operations**: Usually add complexities

### Common Mistakes to Avoid

❌ **Wrong**: Assuming all operations are O(1)  
✅ **Right**: Consider the actual operation complexity

❌ **Wrong**: O(n + n) = O(2n) = O(n)  
✅ **Right**: Correct, but be careful with different inputs

❌ **Wrong**: Hash table operations are always O(1)  
✅ **Right**: O(1) average, O(n) worst case

### Best vs Average vs Worst Case

- **Best Case (Ω)**: Most favorable input
- **Average Case (Θ)**: Expected performance
- **Worst Case (O)**: Most challenging input

*Big O notation typically refers to worst-case complexity*

---

## 🚀 Optimization Strategies

### Time Optimization Techniques

1. **Use Better Data Structures**
   - Hash tables for O(1) lookups
   - Heaps for priority operations
   - Balanced trees for sorted data

2. **Apply Algorithmic Patterns**
   - Two pointers for array problems
   - Sliding window for subarray problems
   - Binary search for sorted data

3. **Caching & Memoization**
   - Store computed results
   - Trade space for time

4. **Divide & Conquer**
   - Break problems into smaller parts
   - Often leads to O(n log n) solutions

### Space Optimization Techniques

1. **In-Place Algorithms**
   - Modify input instead of creating new data
   - Reduce O(n) to O(1) space

2. **Iterative vs Recursive**
   - Avoid call stack overhead
   - Eliminate O(n) recursion depth

3. **Bit Manipulation**
   - Use bits instead of arrays for flags
   - Space-efficient for boolean operations

---

## 📊 Quick Reference Formulas

### Common Patterns

```
Arithmetic Series: 1 + 2 + ... + n = n(n+1)/2 = O(n²)
Geometric Series: 1 + 2 + 4 + ... + 2^k = 2^(k+1) - 1 = O(2^k)
Harmonic Series: 1 + 1/2 + 1/3 + ... + 1/n = O(log n)

Binary Tree Height: log₂(n) for balanced, n for skewed
Complete Binary Tree Nodes: 2^h - 1 (where h is height)
```

### Memory Sizes (Approximate)

```
bool: 1 byte
int: 4 bytes (32-bit) or 8 bytes (64-bit)
float: 4 bytes
double: 8 bytes
pointer: 8 bytes (64-bit system)
```

---

## 🎯 Interview Tips

### What Interviewers Look For

1. **Correct Analysis**: Can you identify the right complexity?
2. **Optimization Awareness**: Do you know when/how to optimize?
3. **Trade-off Understanding**: Space vs time complexity decisions
4. **Pattern Recognition**: Can you identify algorithmic patterns?

### Common Interview Questions

- "What's the time complexity of your solution?"
- "Can you optimize this further?"
- "What's the space complexity?"
- "How does this scale with input size?"
- "What's the best/worst case scenario?"

---

*📚 Master these concepts for efficient algorithm design and technical interviews!*