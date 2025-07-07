# Data Structures Overview 🏗️

Comprehensive overview of fundamental data structures.

## Linear Data Structures

### Arrays
**Definition**: Collection of elements stored in contiguous memory
**Key Properties**:
- Fixed size (static) or dynamic size
- Random access with O(1) indexing
- Cache-friendly due to memory locality

**Use Cases**: 
- Storing homogeneous data
- Mathematical operations
- Implementing other data structures

### Linked Lists
**Definition**: Linear collection where elements point to next element
**Types**:
- **Singly Linked**: Each node points to next
- **Doubly Linked**: Each node points to both next and previous
- **Circular**: Last node points back to first

**Use Cases**:
- Dynamic size requirements
- Frequent insertion/deletion
- Implementing stacks and queues

### Stacks
**Definition**: LIFO (Last In, First Out) data structure
**Key Operations**: Push, Pop, Peek, IsEmpty
**Use Cases**:
- Function call management
- Expression evaluation
- Undo operations in applications
- Depth-first search

### Queues
**Definition**: FIFO (First In, First Out) data structure
**Types**:
- **Simple Queue**: Basic FIFO
- **Circular Queue**: Wrap-around for efficiency
- **Priority Queue**: Elements with priorities
- **Deque**: Double-ended queue

**Use Cases**:
- Task scheduling
- Breadth-first search
- Buffer for asynchronous data transfer

## Non-Linear Data Structures

### Trees
**Definition**: Hierarchical data structure with nodes and edges
**Types**:
- **Binary Tree**: Each node has at most 2 children
- **Binary Search Tree**: Left < Root < Right property
- **AVL Tree**: Self-balancing BST
- **Heap**: Complete binary tree with heap property

**Key Concepts**:
- **Root**: Top node
- **Leaf**: Node with no children
- **Height**: Longest path from root to leaf
- **Depth**: Distance from root to a node

### Graphs
**Definition**: Collection of vertices connected by edges
**Types**:
- **Directed vs Undirected**: Edge direction matters or not
- **Weighted vs Unweighted**: Edges have weights or not
- **Connected vs Disconnected**: All vertices reachable or not

**Representations**:
- **Adjacency Matrix**: 2D array representation
- **Adjacency List**: Array of lists representation

## Hash-Based Structures

### Hash Tables
**Definition**: Data structure using hash function to map keys to values
**Key Concepts**:
- **Hash Function**: Maps keys to array indices
- **Collision**: When two keys hash to same index
- **Load Factor**: Ratio of elements to bucket count

**Collision Resolution**:
- **Chaining**: Store multiple elements in same bucket
- **Open Addressing**: Find next available slot

## Choosing the Right Data Structure

### Performance Considerations
| Operation | Array | Linked List | Hash Table | BST |
|-----------|-------|-------------|------------|-----|
| Access | O(1) | O(n) | O(1)* | O(log n) |
| Search | O(n) | O(n) | O(1)* | O(log n) |
| Insert | O(n) | O(1) | O(1)* | O(log n) |
| Delete | O(n) | O(1) | O(1)* | O(log n) |

*Average case, O(n) worst case

### Decision Framework
1. **Need random access?** → Array
2. **Frequent insertion/deletion?** → Linked List
3. **Need key-value mapping?** → Hash Table
4. **Need sorted order?** → BST
5. **Need LIFO behavior?** → Stack
6. **Need FIFO behavior?** → Queue
7. **Need hierarchical data?** → Tree
8. **Need relationships between entities?** → Graph

## Memory Considerations

### Space Complexity
- **Arrays**: O(n) for n elements
- **Linked Lists**: O(n) + pointer overhead
- **Hash Tables**: O(n) + hash table overhead
- **Trees**: O(n) + pointer overhead
- **Graphs**: O(V + E) for V vertices and E edges

### Cache Performance
- **Good**: Arrays (spatial locality)
- **Poor**: Linked Lists (random memory access)
- **Variable**: Hash Tables (depends on implementation)

## Real-World Applications

### System Design
- **Databases**: B-trees for indexing
- **Caches**: Hash tables with LRU (Doubly Linked List)
- **File Systems**: Trees for directory structure
- **Networks**: Graphs for routing algorithms

### Application Development
- **Undo/Redo**: Stacks for operation history
- **Autocomplete**: Tries for string matching
- **Social Networks**: Graphs for connections
- **Task Scheduling**: Priority queues for job management

## Advanced Topics

### Self-Balancing Trees
- **AVL Trees**: Height-balanced BST
- **Red-Black Trees**: Colored nodes for balance
- **B-Trees**: Multi-way trees for databases

### Specialized Structures
- **Trie**: Tree for string operations
- **Segment Tree**: Range query optimization
- **Disjoint Set**: Union-find operations
- **Bloom Filter**: Probabilistic membership testing
