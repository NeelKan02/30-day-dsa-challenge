# 🎯 Common Problem-Solving Patterns

*Essential patterns and techniques for coding interviews and competitive programming*

---

## 🔄 Pattern 1: Two Pointers

### When to Use
- Array or string problems
- Need to find pairs or triplets
- Searching in sorted arrays
- Palindrome checking

### Common Applications
- Two Sum in sorted array
- Remove duplicates
- Reverse array/string
- Container with most water
- 3Sum problems

### Template
```python
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        if condition_met(arr[left], arr[right]):
            # Process the pair
            return result
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    
    return default_result
```

### Example Problems
- [Two Sum II (#167)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [3Sum (#15)](https://leetcode.com/problems/3sum/)
- [Container With Most Water (#11)](https://leetcode.com/problems/container-with-most-water/)

---

## 🪟 Pattern 2: Sliding Window

### When to Use
- Subarray/substring problems
- Fixed or variable window size
- Min/max subarray problems
- String permutation problems

### Types
1. **Fixed Size Window**: Window size is constant
2. **Variable Size Window**: Window size changes based on condition

### Template - Fixed Size
```python
def sliding_window_fixed(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Template - Variable Size
```python
def sliding_window_variable(arr, target):
    left = 0
    result = float('inf')
    window_sum = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]
        
        while window_sum >= target:
            result = min(result, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return result if result != float('inf') else 0
```

### Example Problems
- [Maximum Average Subarray I (#643)](https://leetcode.com/problems/maximum-average-subarray-i/)
- [Longest Substring Without Repeating Characters (#3)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [Minimum Window Substring (#76)](https://leetcode.com/problems/minimum-window-substring/)

---

## 🔍 Pattern 3: Binary Search

### When to Use
- Sorted arrays
- Search for target or insertion point
- Finding min/max in monotonic function
- Optimization problems with binary answer

### Template - Standard
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
    
    return -1  # Not found
```

### Template - Left Boundary
```python
def find_left_boundary(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

### Example Problems
- [Binary Search (#704)](https://leetcode.com/problems/binary-search/)
- [Search Insert Position (#35)](https://leetcode.com/problems/search-insert-position/)
- [Find Peak Element (#162)](https://leetcode.com/problems/find-peak-element/)

---

## 🌳 Pattern 4: Tree Traversal

### Depth-First Search (DFS)

#### Recursive Template
```python
def dfs_recursive(root):
    if not root:
        return
    
    # Preorder: process current, then children
    process(root)
    dfs_recursive(root.left)
    dfs_recursive(root.right)
```

#### Iterative Template
```python
def dfs_iterative(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        process(node)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### Breadth-First Search (BFS)

```python
def bfs(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            process(node)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

### Example Problems
- [Binary Tree Inorder Traversal (#94)](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [Binary Tree Level Order Traversal (#102)](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [Maximum Depth of Binary Tree (#104)](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## 🔄 Pattern 5: Backtracking

### When to Use
- Generate all possible solutions
- Find all permutations/combinations
- Constraint satisfaction problems
- Maze/path finding problems

### Template
```python
def backtrack(path, choices):
    # Base case
    if is_solution(path):
        result.append(path[:])  # Make a copy
        return
    
    for choice in choices:
        if is_valid(choice, path):
            # Make choice
            path.append(choice)
            
            # Recurse
            backtrack(path, get_new_choices(choices, choice))
            
            # Undo choice (backtrack)
            path.pop()
```

### Example Problems
- [Permutations (#46)](https://leetcode.com/problems/permutations/)
- [Combinations (#77)](https://leetcode.com/problems/combinations/)
- [N-Queens (#51)](https://leetcode.com/problems/n-queens/)

---

## 📊 Pattern 6: Dynamic Programming

### When to Use
- Optimization problems (min/max)
- Counting problems
- Decision problems
- Problems with overlapping subproblems

### 1D DP Template
```python
def dp_1d(arr):
    n = len(arr)
    dp = [0] * n
    
    # Base case
    dp[0] = arr[0]
    
    for i in range(1, n):
        dp[i] = max(dp[i-1], arr[i])  # Recurrence relation
    
    return dp[n-1]
```

### 2D DP Template
```python
def dp_2d(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    
    # Base cases
    dp[0][0] = matrix[0][0]
    
    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + matrix[i][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + matrix[i][j])
    
    return dp[m-1][n-1]
```

### Example Problems
- [Fibonacci Number (#509)](https://leetcode.com/problems/fibonacci-number/)
- [Climbing Stairs (#70)](https://leetcode.com/problems/climbing-stairs/)
- [Unique Paths (#62)](https://leetcode.com/problems/unique-paths/)

---

## 🌐 Pattern 7: Graph Algorithms

### DFS Template
```python
def dfs_graph(graph, start, visited):
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited)
```

### BFS Template
```python
def bfs_graph(graph, start):
    visited = set([start])
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### Union-Find Template
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
            px, py = py, px
        
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        
        return True
```

---

## 🎲 Pattern 8: Hash Map/Set Patterns

### Frequency Counter
```python
def frequency_pattern(arr):
    freq = {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    
    # Process based on frequencies
    return process_frequencies(freq)
```

### Two Sum Pattern
```python
def two_sum_pattern(arr, target):
    seen = {}
    
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []
```

### Sliding Window with Hash Map
```python
def sliding_window_hash(s, pattern):
    window = {}
    need = {}
    
    for char in pattern:
        need[char] = need.get(char, 0) + 1
    
    left = right = 0
    valid = 0
    
    while right < len(s):
        char = s[right]
        right += 1
        
        if char in need:
            window[char] = window.get(char, 0) + 1
            if window[char] == need[char]:
                valid += 1
        
        while valid == len(need):
            # Process valid window
            
            char = s[left]
            left += 1
            
            if char in need:
                if window[char] == need[char]:
                    valid -= 1
                window[char] -= 1
```

---

## 🔢 Pattern 9: Mathematical Patterns

### GCD/LCM
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
```

### Prime Checking
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### Fast Exponentiation
```python
def power(base, exp, mod=None):
    result = 1
    base = base % mod if mod else base
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod if mod else result * base
        exp = exp >> 1
        base = (base * base) % mod if mod else base * base
    
    return result
```

---

## 🎯 Pattern Selection Guide

### Problem Type → Pattern Mapping

| Problem Characteristics | Recommended Pattern |
|-------------------------|-------------------|
| Sorted array, find target | Binary Search |
| Two elements sum to target | Two Pointers |
| Subarray/substring optimization | Sliding Window |
| Generate all possibilities | Backtracking |
| Optimization with overlapping subproblems | Dynamic Programming |
| Tree/graph traversal | DFS/BFS |
| Fast lookups/counting | Hash Map/Set |
| Connected components | Union-Find |

### Time Complexity Goals

| Input Size | Target Complexity | Suitable Patterns |
|------------|------------------|------------------|
| n ≤ 20 | O(2ⁿ) | Backtracking, brute force |
| n ≤ 100 | O(n³) | Triple loops, some DP |
| n ≤ 1,000 | O(n²) | Double loops, 2D DP |
| n ≤ 100,000 | O(n log n) | Sorting, binary search, divide & conquer |
| n ≤ 1,000,000 | O(n) | Linear algorithms, hash maps |
| n > 1,000,000 | O(log n) or O(1) | Binary search, math formulas |

---

## 🚀 Advanced Techniques

### Bit Manipulation Patterns
```python
# Check if power of 2
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Count set bits
def count_bits(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count

# Get/set/clear bit
def get_bit(n, i): return (n >> i) & 1
def set_bit(n, i): return n | (1 << i)
def clear_bit(n, i): return n & ~(1 << i)
```

### String Processing Patterns
```python
# KMP Pattern Matching
def kmp_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = build_lps(pattern)
    # ... rest of KMP implementation
```

---

*🎯 Master these patterns to solve 80% of coding interview problems efficiently!*