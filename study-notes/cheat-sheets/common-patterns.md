# Common Algorithm Patterns 🎯

Essential patterns for solving algorithmic problems efficiently.

## Array Patterns

### Two Pointers
**When to use**: Array problems with sorted data or searching pairs
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

### Sliding Window
**When to use**: Subarray/substring problems with contiguous elements
```python
def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Fast & Slow Pointers
**When to use**: Cycle detection, finding middle element
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## Tree Patterns

### DFS Traversals
```python
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
```

### BFS Level Order
```python
def level_order(root):
    if not root:
        return []
    
    result, queue = [], [root]
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

## Dynamic Programming Patterns

### Top-Down (Memoization)
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]
```

### Bottom-Up (Tabulation)
```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## Problem-Solving Templates

### Binary Search Template
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

### Backtracking Template
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, updated_choices)
            path.pop()  # backtrack
```
