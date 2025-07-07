# Algorithms Overview 🔬

Comprehensive overview of fundamental algorithms and their applications.

## Algorithm Analysis

### Time Complexity Classes
- **O(1)**: Constant time - Hash table lookup
- **O(log n)**: Logarithmic - Binary search
- **O(n)**: Linear - Array traversal
- **O(n log n)**: Linearithmic - Efficient sorting
- **O(n²)**: Quadratic - Nested loops
- **O(2ⁿ)**: Exponential - Recursive algorithms

### Space Complexity
- **In-place**: O(1) extra space
- **Linear**: O(n) extra space
- **Logarithmic**: O(log n) for recursion stack

## Sorting Algorithms

### Comparison-Based Sorts

#### Bubble Sort
- **Time**: O(n²) average and worst, O(n) best
- **Space**: O(1)
- **Stable**: Yes
- **Use**: Educational purposes only

#### Selection Sort
- **Time**: O(n²) all cases
- **Space**: O(1)
- **Stable**: No
- **Use**: Small datasets, memory-constrained

#### Insertion Sort
- **Time**: O(n²) average and worst, O(n) best
- **Space**: O(1)
- **Stable**: Yes
- **Use**: Small or nearly sorted arrays

#### Merge Sort
- **Time**: O(n log n) all cases
- **Space**: O(n)
- **Stable**: Yes
- **Use**: When stability is required, guaranteed performance

#### Quick Sort
- **Time**: O(n log n) average, O(n²) worst
- **Space**: O(log n) average
- **Stable**: No
- **Use**: General-purpose sorting, cache-efficient

#### Heap Sort
- **Time**: O(n log n) all cases
- **Space**: O(1)
- **Stable**: No
- **Use**: When space is limited, guaranteed performance

### Non-Comparison Sorts

#### Counting Sort
- **Time**: O(n + k) where k is range
- **Space**: O(k)
- **Use**: Small integer ranges

#### Radix Sort
- **Time**: O(nk) where k is digit count
- **Space**: O(n + k)
- **Use**: Fixed-width integers or strings

## Search Algorithms

### Linear Search
- **Time**: O(n)
- **Space**: O(1)
- **Use**: Unsorted data, small datasets

### Binary Search
- **Time**: O(log n)
- **Space**: O(1) iterative, O(log n) recursive
- **Requirements**: Sorted data
- **Use**: Sorted arrays, search optimization

### Depth-First Search (DFS)
- **Time**: O(V + E) for graphs
- **Space**: O(V) for recursion stack
- **Use**: Tree/graph traversal, topological sort

### Breadth-First Search (BFS)
- **Time**: O(V + E) for graphs
- **Space**: O(V) for queue
- **Use**: Shortest path (unweighted), level-order traversal

## Dynamic Programming

### Characteristics
- **Optimal Substructure**: Solution contains optimal sub-solutions
- **Overlapping Subproblems**: Same subproblems solved multiple times

### Approaches

#### Top-Down (Memoization)
```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return memo[n]
```

#### Bottom-Up (Tabulation)
```python
def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### Common DP Problems
- **Fibonacci Sequence**: Classic example
- **Knapsack Problem**: Resource optimization
- **Longest Common Subsequence**: String similarity
- **Coin Change**: Minimum coins for amount

## Greedy Algorithms

### Characteristics
- **Local Optimal Choice**: Make best choice at each step
- **No Backtracking**: Decisions are final
- **Optimal Substructure**: Local optimums lead to global optimum

### Common Applications
- **Activity Selection**: Schedule non-overlapping activities
- **Huffman Coding**: Optimal prefix codes
- **Minimum Spanning Tree**: Kruskal's and Prim's algorithms
- **Dijkstra's Algorithm**: Shortest path in weighted graphs

## Graph Algorithms

### Traversal Algorithms
- **DFS**: Stack-based or recursive
- **BFS**: Queue-based, level-by-level

### Shortest Path Algorithms

#### Dijkstra's Algorithm
- **Time**: O((V + E) log V) with binary heap
- **Space**: O(V)
- **Use**: Non-negative weighted graphs
- **Single-source shortest path**

#### Bellman-Ford Algorithm
- **Time**: O(VE)
- **Space**: O(V)
- **Use**: Graphs with negative weights
- **Detects negative cycles**

#### Floyd-Warshall Algorithm
- **Time**: O(V³)
- **Space**: O(V²)
- **Use**: All-pairs shortest paths
- **Works with negative weights**

### Minimum Spanning Tree

#### Kruskal's Algorithm
- **Approach**: Sort edges, use Union-Find
- **Time**: O(E log E)
- **Space**: O(V)

#### Prim's Algorithm
- **Approach**: Grow tree from starting vertex
- **Time**: O((V + E) log V) with binary heap
- **Space**: O(V)

### Topological Sorting
- **Use**: Dependency resolution, task scheduling
- **Requirements**: Directed Acyclic Graph (DAG)
- **Algorithms**: DFS-based, Kahn's algorithm

## Divide and Conquer

### Strategy
1. **Divide**: Break problem into smaller subproblems
2. **Conquer**: Solve subproblems recursively
3. **Combine**: Merge solutions of subproblems

### Examples
- **Merge Sort**: Divide array, sort halves, merge
- **Quick Sort**: Partition around pivot, sort parts
- **Binary Search**: Divide search space in half
- **Closest Pair**: Divide points, find closest in each half

## Backtracking

### Strategy
- **Try**: Make a choice
- **Check**: Verify if choice leads to solution
- **Backtrack**: Undo choice if it doesn't work
- **Repeat**: Try next possibility

### Common Problems
- **N-Queens**: Place queens on chessboard
- **Sudoku Solver**: Fill grid with constraints
- **Permutations**: Generate all arrangements
- **Subset Sum**: Find subset with target sum

## Algorithm Design Paradigms

### When to Use Each Paradigm

#### Greedy
- **When**: Local optimal leads to global optimal
- **Examples**: Activity selection, Huffman coding

#### Dynamic Programming
- **When**: Optimal substructure + overlapping subproblems
- **Examples**: Knapsack, longest subsequence

#### Divide and Conquer
- **When**: Problem can be broken into independent subproblems
- **Examples**: Merge sort, binary search

#### Backtracking
- **When**: Need to explore all possibilities with constraints
- **Examples**: N-Queens, Sudoku

## Complexity Analysis Tips

### Best, Average, Worst Case
- **Best Case**: Most favorable input
- **Average Case**: Expected performance over all inputs
- **Worst Case**: Least favorable input

### Amortized Analysis
- **Purpose**: Average time per operation over sequence
- **Example**: Dynamic array append is O(1) amortized

### Space-Time Tradeoffs
- **More Space**: Often reduces time complexity
- **Examples**: Memoization, hash tables
- **Consideration**: Memory constraints vs speed requirements

## Practical Considerations

### Algorithm Selection
1. **Input Size**: Different algorithms optimal for different sizes
2. **Data Characteristics**: Sorted, nearly sorted, random
3. **Memory Constraints**: In-place vs extra space
4. **Stability Requirements**: Maintain relative order
5. **Online vs Offline**: Process data as it arrives vs all at once

### Implementation Tips
- **Start Simple**: Get correct solution first
- **Optimize**: Improve time/space complexity
- **Test**: Edge cases, large inputs, empty inputs
- **Profile**: Measure actual performance
