# 🔬 Algorithms Overview

*Comprehensive guide to fundamental algorithms for the 30-day challenge*

---

## 🎯 Algorithm Classification

### By Design Strategy
- **Brute Force:** Try all possibilities
- **Divide & Conquer:** Break into smaller subproblems
- **Dynamic Programming:** Solve overlapping subproblems
- **Greedy:** Make locally optimal choices
- **Backtracking:** Systematically try all possibilities

### By Problem Domain
- **Sorting:** Arrange data in order
- **Searching:** Find specific elements
- **Graph:** Navigate and analyze connections
- **String:** Process and manipulate text
- **Mathematical:** Compute numerical results

---

## 🔀 Sorting Algorithms

### Comparison-Based Sorting

#### 🫧 Bubble Sort
**Algorithm:** Repeatedly compare adjacent elements and swap if in wrong order.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)  
**Stable:** Yes  
**Use Case:** Educational purposes, small datasets

---

#### 🎯 Selection Sort
**Algorithm:** Find minimum element and place it at beginning, repeat for remaining array.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)  
**Stable:** No  
**Use Case:** Small datasets, minimal swaps needed

---

#### 📥 Insertion Sort
**Algorithm:** Build sorted array one element at a time by inserting each element in correct position.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

**Time Complexity:** O(n²) worst, O(n) best  
**Space Complexity:** O(1)  
**Stable:** Yes  
**Use Case:** Small datasets, nearly sorted data, online algorithm

---

#### 🔀 Merge Sort
**Algorithm:** Divide array in half, recursively sort both halves, then merge sorted halves.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)  
**Stable:** Yes  
**Use Case:** Large datasets, guaranteed performance, stable sorting needed

---

#### ⚡ Quick Sort
**Algorithm:** Choose pivot, partition array around pivot, recursively sort partitions.

```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**Time Complexity:** O(n log n) average, O(n²) worst  
**Space Complexity:** O(log n)  
**Stable:** No  
**Use Case:** General purpose, in-place sorting, average case performance

---

#### 🏔️ Heap Sort
**Algorithm:** Build max heap, repeatedly extract maximum and place at end.

```python
def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)  
**Stable:** No  
**Use Case:** Guaranteed performance, memory constrained

---

### Non-Comparison Sorting

#### 🔢 Counting Sort
**Algorithm:** Count occurrences of each element, use counts to place elements in sorted order.

```python
def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    count = [0] * range_val
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Reconstruct sorted array
    result = []
    for i, cnt in enumerate(count):
        result.extend([i + min_val] * cnt)
    
    return result
```

**Time Complexity:** O(n + k) where k is range  
**Space Complexity:** O(k)  
**Stable:** Yes  
**Use Case:** Small range of integers, known range

---

#### 🌟 Radix Sort
**Algorithm:** Sort by individual digits/characters from least to most significant.

```python
def radix_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    # Calculate positions
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]
```

**Time Complexity:** O(d × (n + k)) where d is digits, k is base  
**Space Complexity:** O(n + k)  
**Stable:** Yes  
**Use Case:** Integer sorting, string sorting with fixed length

---

## 🔍 Searching Algorithms

### 📏 Linear Search
**Algorithm:** Check each element sequentially until target is found.

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

**Time Complexity:** O(n)  
**Space Complexity:** O(1)  
**Use Case:** Unsorted data, small datasets

---

### 🎯 Binary Search
**Algorithm:** Repeatedly divide search space in half by comparing with middle element.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

**Time Complexity:** O(log n)  
**Space Complexity:** O(1)  
**Prerequisite:** Sorted array  
**Use Case:** Sorted data, large datasets

---

### 🔍 Binary Search Variants

#### Find First Occurrence
```python
def find_first(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left if left < len(arr) and arr[left] == target else -1
```

#### Find Last Occurrence
```python
def find_last(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left - 1 if left > 0 and arr[left - 1] == target else -1
```

---

## 🌐 Graph Algorithms

### 📊 Graph Traversal

#### 🔍 Depth-First Search (DFS)
**Algorithm:** Explore as far as possible along each branch before backtracking.

```python
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Add neighbors in reverse order for consistent ordering
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
```

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V)  
**Use Case:** Topological sorting, cycle detection, maze solving

---

#### 🌊 Breadth-First Search (BFS)
**Algorithm:** Explore neighbors before moving to next level.

```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result
```

**Time Complexity:** O(V + E)  
**Space Complexity:** O(V)  
**Use Case:** Shortest path in unweighted graphs, level-order traversal

---

### 🛤️ Shortest Path Algorithms

#### 🎯 Dijkstra's Algorithm
**Algorithm:** Find shortest path from source to all vertices (non-negative weights).

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor, weight in graph[current]:
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

**Time Complexity:** O((V + E) log V)  
**Space Complexity:** O(V)  
**Use Case:** GPS navigation, network routing

---

#### ⚡ Bellman-Ford Algorithm
**Algorithm:** Find shortest path from source (handles negative weights).

```python
def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative cycle")
    
    return distances
```

**Time Complexity:** O(VE)  
**Space Complexity:** O(V)  
**Use Case:** Currency exchange, negative weight edges

---

#### 🔄 Floyd-Warshall Algorithm
**Algorithm:** Find shortest paths between all pairs of vertices.

```python
def floyd_warshall(graph):
    nodes = list(graph.keys())
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}
    
    # Initialize distances
    for i in nodes:
        dist[i][i] = 0
        for j, weight in graph[i]:
            dist[i][j] = weight
    
    # Main algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

**Time Complexity:** O(V³)  
**Space Complexity:** O(V²)  
**Use Case:** Dense graphs, all-pairs shortest paths

---

### 🌳 Minimum Spanning Tree

#### 🔗 Kruskal's Algorithm
**Algorithm:** Sort edges by weight, add edges that don't create cycles.

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        return True

def kruskal(vertices, edges):
    uf = UnionFind(len(vertices))
    edges.sort(key=lambda x: x[2])  # Sort by weight
    mst = []
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            if len(mst) == len(vertices) - 1:
                break
    
    return mst
```

**Time Complexity:** O(E log E)  
**Space Complexity:** O(V)  
**Use Case:** Sparse graphs, network design

---

#### 🌿 Prim's Algorithm
**Algorithm:** Grow MST by adding minimum weight edge to tree.

```python
import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(edges)
    
    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            
            for neighbor, w in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
    
    return mst
```

**Time Complexity:** O(E log V)  
**Space Complexity:** O(V)  
**Use Case:** Dense graphs, network design

---

## 🎯 Dynamic Programming

### 🧠 Core Concepts

**When to Use DP:**
1. **Optimal Substructure:** Optimal solution contains optimal solutions to subproblems
2. **Overlapping Subproblems:** Same subproblems are solved multiple times

**DP Approaches:**
1. **Top-Down (Memoization):** Recursive with caching
2. **Bottom-Up (Tabulation):** Iterative with table

### 📈 Classic DP Problems

#### 🏃‍♂️ Fibonacci Sequence
```python
# Memoization
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Tabulation
def fibonacci_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

#### 🪜 Climbing Stairs
```python
def climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

#### 🎒 0/1 Knapsack
```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # Include item
                    dp[i-1][w]  # Exclude item
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

#### 🛤️ Longest Common Subsequence
```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]
```

---

## 🏃‍♂️ Greedy Algorithms

### 🎯 When to Use Greedy
- Problem has optimal substructure
- Greedy choice property: Local optimum leads to global optimum
- No need to reconsider previous choices

### 💰 Classic Greedy Problems

#### 🪙 Coin Change (Greedy)
```python
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        if amount >= coin:
            count += amount // coin
            amount %= coin
    
    return count if amount == 0 else -1
```

#### 📅 Activity Selection
```python
def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected
```

---

## 🔄 Backtracking

### 🎯 Template
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])  # Add copy of solution
        return
    
    for choice in choices:
        if is_valid(choice, path):
            path.append(choice)  # Make choice
            backtrack(path, get_new_choices(choices, choice))
            path.pop()  # Undo choice
```

### 👑 N-Queens Problem
```python
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check column
        for i in range(row):
            if board[i] == col:
                return False
        
        # Check diagonals
        for i in range(row):
            if abs(board[i] - col) == abs(i - row):
                return False
        
        return True
    
    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
    
    result = []
    backtrack([-1] * n, 0)
    return result
```

---

## 🎯 Algorithm Selection Guide

### Time Complexity Goals
| Problem Size | Target Complexity | Suitable Algorithms |
|-------------|------------------|-------------------|
| n ≤ 10 | O(n!) | Permutations, brute force |
| n ≤ 20 | O(2ⁿ) | DP with bitmask, backtracking |
| n ≤ 100 | O(n³) | Floyd-Warshall, matrix operations |
| n ≤ 1,000 | O(n²) | DP, nested loops |
| n ≤ 100,000 | O(n log n) | Sorting, divide & conquer |
| n ≤ 1,000,000 | O(n) | Linear algorithms, hash tables |

### Problem Type Mapping
| Problem Type | Best Algorithm Strategy |
|-------------|----------------------|
| Shortest Path | Dijkstra's, BFS, Bellman-Ford |
| Sorting | Merge Sort, Quick Sort, Heap Sort |
| Searching | Binary Search, Hash Table |
| Optimization | Dynamic Programming, Greedy |
| Combinatorial | Backtracking, DFS |
| Graph Connectivity | DFS, BFS, Union-Find |

---

*🔬 Master these algorithms to solve complex computational problems efficiently!*