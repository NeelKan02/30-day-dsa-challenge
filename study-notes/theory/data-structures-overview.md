# 📊 Data Structures Overview

*Comprehensive guide to fundamental data structures for the 30-day challenge*

---

## 🎯 Data Structure Classification

### Linear Data Structures
Data elements are arranged sequentially, each element connects to the next.

### Non-Linear Data Structures  
Data elements are not arranged sequentially, elements can connect to multiple others.

---

## 📚 Linear Data Structures

### 🔢 Arrays

**Definition:** Collection of elements stored in contiguous memory locations.

**Key Characteristics:**
- Fixed size (static arrays) or dynamic size (dynamic arrays)
- Elements accessed by index
- Homogeneous data type
- Random access capability

**Time Complexities:**
| Operation | Time Complexity |
|-----------|----------------|
| Access | O(1) |
| Search | O(n) |
| Insertion | O(n) |
| Deletion | O(n) |

**Space Complexity:** O(n)

**Use Cases:**
- Storing collections of similar data
- Mathematical operations (matrices)
- Implementing other data structures
- Lookup tables and caching

**Advantages:**
- Fast random access
- Memory efficient
- Simple iteration
- Cache-friendly access patterns

**Disadvantages:**
- Fixed size (static arrays)
- Expensive insertion/deletion
- Memory waste if not fully utilized

---

### 🔗 Linked Lists

**Definition:** Linear collection where elements (nodes) are stored in sequence, each pointing to the next.

#### Types:

**1. Singly Linked List**
- Each node has data and pointer to next node
- Forward traversal only
- Last node points to null

**2. Doubly Linked List**
- Each node has data, next pointer, and previous pointer
- Bidirectional traversal
- More memory overhead

**3. Circular Linked List**
- Last node points back to first node
- No null pointers
- Continuous traversal possible

**Time Complexities:**
| Operation | Time Complexity |
|-----------|----------------|
| Access | O(n) |
| Search | O(n) |
| Insertion | O(1) at given position |
| Deletion | O(1) at given position |

**Space Complexity:** O(n)

**Use Cases:**
- Dynamic memory allocation
- Implementing stacks and queues
- Music playlist (circular)
- Undo functionality in applications

**Advantages:**
- Dynamic size
- Efficient insertion/deletion
- Memory efficient (allocate as needed)

**Disadvantages:**
- No random access
- Extra memory for pointers
- Not cache-friendly
- Vulnerable to memory leaks

---

### 📚 Stacks

**Definition:** Linear data structure following Last-In-First-Out (LIFO) principle.

**Core Operations:**
- **Push:** Add element to top
- **Pop:** Remove element from top  
- **Peek/Top:** View top element without removing
- **isEmpty:** Check if stack is empty

**Time Complexities:**
| Operation | Time Complexity |
|-----------|----------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

**Space Complexity:** O(n)

**Use Cases:**
- Function call management (call stack)
- Expression evaluation and parsing
- Undo operations
- Browser history
- Backtracking algorithms

**Implementation Methods:**
- Array-based (fixed size)
- Linked list-based (dynamic size)

**Advantages:**
- Simple to implement
- Efficient push/pop operations
- Memory efficient
- Natural for recursive problems

**Disadvantages:**
- Limited access (only top element)
- Can cause stack overflow
- Not suitable for searching

---

### 🏪 Queues

**Definition:** Linear data structure following First-In-First-Out (FIFO) principle.

**Core Operations:**
- **Enqueue:** Add element to rear
- **Dequeue:** Remove element from front
- **Front:** View front element
- **Rear:** View rear element
- **isEmpty:** Check if queue is empty

#### Types:

**1. Simple Queue**
- Basic FIFO operations
- Fixed size limitation

**2. Circular Queue**
- Rear connects back to front
- Efficient space utilization
- Overcomes simple queue limitations

**3. Priority Queue**
- Elements have priorities
- High priority elements served first
- Implemented using heaps

**4. Double-Ended Queue (Deque)**
- Insertion/deletion at both ends
- Combines stack and queue features

**Time Complexities:**
| Operation | Time Complexity |
|-----------|----------------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front/Rear | O(1) |
| Search | O(n) |

**Space Complexity:** O(n)

**Use Cases:**
- Process scheduling (OS)
- Breadth-First Search (BFS)
- Handling requests in web servers
- Print job management
- Traffic management systems

**Advantages:**
- Fair ordering (FIFO)
- Efficient for producer-consumer problems
- Simple to implement
- Memory efficient

**Disadvantages:**
- Limited access (only front/rear)
- Can waste memory (simple queue)
- Not suitable for searching

---

## 🗂️ Hash-Based Data Structures

### 🔐 Hash Tables

**Definition:** Data structure that implements associative array, mapping keys to values using hash function.

**Key Components:**
- **Hash Function:** Converts key to array index
- **Buckets:** Array positions storing key-value pairs
- **Collision Resolution:** Handling multiple keys mapping to same bucket

**Hash Functions:**
- Division method: `h(key) = key % table_size`
- Multiplication method: `h(key) = floor(table_size * (key * A % 1))`
- Universal hashing: Randomized hash functions

**Collision Resolution:**

**1. Chaining (Open Hashing)**
- Store multiple elements in linked list at each bucket
- Simple to implement
- Dynamic memory usage

**2. Open Addressing (Closed Hashing)**
- Find alternative bucket for collisions
- Linear probing: Check next bucket
- Quadratic probing: Check i² positions away
- Double hashing: Use second hash function

**Time Complexities:**
| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Search | O(1) | O(n) |
| Insertion | O(1) | O(n) |
| Deletion | O(1) | O(n) |

**Space Complexity:** O(n)

**Load Factor:** α = n/m (n = elements, m = buckets)
- Optimal load factor: 0.7-0.8
- Higher load factor → more collisions
- Lower load factor → memory waste

**Use Cases:**
- Database indexing
- Caches and memoization
- Symbol tables in compilers
- Set implementation
- Dictionary/map implementation

**Advantages:**
- Fast average-case operations
- Flexible key types
- Efficient for sparse data
- Dynamic sizing

**Disadvantages:**
- Worst-case performance can be poor
- Memory overhead
- Not suitable for ordered operations
- Hash function design complexity

---

## 🌳 Non-Linear Data Structures

### 🌲 Trees

**Definition:** Hierarchical data structure with nodes connected by edges, forming parent-child relationships.

**Tree Terminology:**
- **Root:** Top node with no parent
- **Leaf:** Node with no children
- **Height:** Maximum depth from root to leaf
- **Depth:** Distance from root to specific node
- **Subtree:** Tree rooted at any node

#### Binary Trees

**Definition:** Tree where each node has at most two children (left and right).

**Types:**

**1. Full Binary Tree**
- Every node has 0 or 2 children
- No nodes with exactly 1 child

**2. Complete Binary Tree**
- All levels filled except possibly the last
- Last level filled from left to right

**3. Perfect Binary Tree**
- All internal nodes have 2 children
- All leaves at same level

**4. Balanced Binary Tree**
- Height difference between left and right subtrees ≤ 1
- Examples: AVL tree, Red-Black tree

**Tree Traversals:**

**1. Depth-First Search (DFS)**
- **Preorder:** Root → Left → Right
- **Inorder:** Left → Root → Right (gives sorted order in BST)
- **Postorder:** Left → Right → Root

**2. Breadth-First Search (BFS)**
- **Level-order:** Visit nodes level by level

**Time Complexities:**
| Operation | Average | Worst Case |
|-----------|---------|------------|
| Search | O(log n) | O(n) |
| Insertion | O(log n) | O(n) |
| Deletion | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

**Space Complexity:** O(n)

#### Binary Search Trees (BST)

**Definition:** Binary tree where left subtree contains values less than root, right subtree contains values greater than root.

**BST Property:**
For any node n:
- All values in left subtree < n.value
- All values in right subtree > n.value
- Both subtrees are also BSTs

**Operations:**

**Search:**
```python
def search(root, key):
    if not root or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)
```

**Insertion:**
```python
def insert(root, key):
    if not root:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
```

**Use Cases:**
- Sorted data storage
- Database indexing
- Expression parsing
- Decision trees
- File systems

**Advantages:**
- Efficient searching in sorted data
- Dynamic size
- In-order traversal gives sorted sequence
- Supports range queries

**Disadvantages:**
- Can become unbalanced (degrades to O(n))
- Complex deletion operation
- No constant-time operations
- Memory overhead for pointers

---

### ⛰️ Heaps

**Definition:** Complete binary tree satisfying heap property.

**Heap Property:**
- **Max Heap:** Parent ≥ children (root is maximum)
- **Min Heap:** Parent ≤ children (root is minimum)

**Implementation:** Usually as array/list
- Parent of index i: `(i-1)//2`
- Left child of index i: `2*i + 1`
- Right child of index i: `2*i + 2`

**Operations:**

**Insertion (Bubble Up):**
1. Add element at end
2. Compare with parent
3. Swap if heap property violated
4. Repeat until property satisfied

**Deletion (Bubble Down):**
1. Replace root with last element
2. Remove last element
3. Compare with children
4. Swap with appropriate child
5. Repeat until property satisfied

**Time Complexities:**
| Operation | Time Complexity |
|-----------|----------------|
| Find Min/Max | O(1) |
| Insertion | O(log n) |
| Deletion | O(log n) |
| Build Heap | O(n) |

**Space Complexity:** O(n)

**Use Cases:**
- Priority queues
- Heap sort algorithm
- Graph algorithms (Dijkstra's, Prim's)
- Job scheduling
- Memory management

**Advantages:**
- Efficient priority operations
- Space efficient (array implementation)
- Guaranteed log n insertion/deletion
- Easy to implement

**Disadvantages:**
- No efficient searching
- Not suitable for sorted traversal
- Limited flexibility compared to BST

---

### 📊 Graphs

**Definition:** Collection of vertices (nodes) connected by edges.

**Graph Components:**
- **Vertices (V):** Set of nodes
- **Edges (E):** Set of connections between vertices
- **Degree:** Number of edges connected to a vertex

**Types:**

**1. Directed vs Undirected**
- **Directed:** Edges have direction (A → B)
- **Undirected:** Edges are bidirectional (A ↔ B)

**2. Weighted vs Unweighted**
- **Weighted:** Edges have associated values/costs
- **Unweighted:** All edges have equal weight

**3. Connected vs Disconnected**
- **Connected:** Path exists between every pair of vertices
- **Disconnected:** Some vertices unreachable from others

**4. Cyclic vs Acyclic**
- **Cyclic:** Contains at least one cycle
- **Acyclic:** No cycles (DAG - Directed Acyclic Graph)

**Representations:**

**1. Adjacency Matrix**
- 2D array where matrix[i][j] = 1 if edge exists
- Space: O(V²)
- Good for dense graphs

**2. Adjacency List**
- Array of lists, each list contains neighbors
- Space: O(V + E)
- Good for sparse graphs

**3. Edge List**
- List of all edges as pairs (u, v)
- Space: O(E)
- Simple but limited functionality

**Graph Algorithms:**

**Traversal:**
- **Depth-First Search (DFS):** Explore as far as possible before backtracking
- **Breadth-First Search (BFS):** Explore neighbors before going deeper

**Shortest Path:**
- **Dijkstra's Algorithm:** Single-source shortest path (non-negative weights)
- **Bellman-Ford:** Single-source shortest path (handles negative weights)
- **Floyd-Warshall:** All-pairs shortest path

**Minimum Spanning Tree:**
- **Kruskal's Algorithm:** Sort edges, add if no cycle
- **Prim's Algorithm:** Grow tree from arbitrary vertex

**Time Complexities:**
| Algorithm | Time Complexity |
|-----------|----------------|
| DFS/BFS | O(V + E) |
| Dijkstra's | O((V + E) log V) |
| Bellman-Ford | O(VE) |
| Floyd-Warshall | O(V³) |
| Kruskal's | O(E log E) |
| Prim's | O(E log V) |

**Use Cases:**
- Social networks
- Computer networks
- Maps and navigation
- Dependencies (task scheduling)
- Web page linking
- Chemical compounds

**Advantages:**
- Models complex relationships
- Flexible structure
- Rich algorithmic possibilities
- Natural for many real-world problems

**Disadvantages:**
- Can be memory intensive
- Complex algorithms
- Difficult to optimize for cache
- May require sophisticated algorithms

---

## 🎯 Choosing the Right Data Structure

### Decision Framework

**Consider These Factors:**
1. **Operations Needed:** What operations will be frequent?
2. **Time Requirements:** What's the acceptable time complexity?
3. **Space Constraints:** How much memory is available?
4. **Data Characteristics:** Size, distribution, patterns
5. **Access Patterns:** Random, sequential, or structured access

### Quick Decision Guide

| Need | Best Data Structure |
|------|-------------------|
| Fast random access | Array |
| Dynamic size with fast insertion | Linked List, Dynamic Array |
| LIFO operations | Stack |
| FIFO operations | Queue |
| Fast lookup by key | Hash Table |
| Sorted data with fast search | BST, Balanced Tree |
| Priority-based access | Heap |
| Complex relationships | Graph |
| Range queries | Segment Tree, Fenwick Tree |

### Performance Summary

| Data Structure | Access | Search | Insert | Delete | Space |
|----------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | N/A | O(1)* | O(1)* | O(1)* | O(n) |
| BST | O(log n)* | O(log n)* | O(log n)* | O(log n)* | O(n) |
| Heap | N/A | O(n) | O(log n) | O(log n) | O(n) |

*Average case; worst case may be higher

---

*📚 Master these data structures to build a strong foundation for algorithm design and problem-solving!*