# 📚 Day 1 - Arrays Foundation

**Date:** July 7, 2025  
**Focus Topic:** Arrays & Dynamic Arrays  
**Time Allocated:** 1.5 hours  
**Status:** 🔥 **IN PROGRESS**

---

## 🎯 Today's Learning Objectives

### Theory Goals (45 minutes)
- [x] Understand array memory layout and indexing
- [x] Learn array time complexities (access, search, insertion, deletion)
- [x] Study dynamic array concepts and implementation
- [x] Compare static vs dynamic arrays

### Implementation Goals (45 minutes) 
- [x] Implement a dynamic array class in Python
- [x] Include methods: append, insert, delete, resize
- [x] Add proper error handling and edge cases
- [x] Write basic test cases for verification

### Problem-Solving Goals (45 minutes)
**Target: 5 LeetCode Problems**
- [x] [Two Sum (#1)](https://leetcode.com/problems/two-sum/) - Easy
- [x] [Remove Duplicates from Sorted Array (#26)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) - Easy  
- [x] [Best Time to Buy and Sell Stock (#121)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Easy
- [x] [Rotate Array (#189)](https://leetcode.com/problems/rotate-array/) - Medium
- [x] [Contains Duplicate (#217)](https://leetcode.com/problems/contains-duplicate/) - Easy

---

## 📖 Theory Study Session

### Array Fundamentals

**Memory Layout:**
- Arrays store elements in contiguous memory locations
- Each element can be accessed in O(1) time using index
- Index calculation: `base_address + (index * element_size)`

**Time Complexities:**
| Operation | Time Complexity | Explanation |
|-----------|----------------|-------------|
| Access | O(1) | Direct index calculation |
| Search | O(n) | May need to check all elements |
| Insertion | O(n) | May need to shift elements |
| Deletion | O(n) | May need to shift elements |

**Space Complexity:** O(n) where n is the number of elements

### Dynamic Arrays vs Static Arrays

**Static Arrays:**
- Fixed size determined at compile time
- Memory allocated on stack (for small arrays)
- Cannot change size after creation

**Dynamic Arrays:**
- Size can change during runtime
- Memory allocated on heap
- Automatic resizing when capacity is exceeded
- Examples: Python lists, C++ vectors, Java ArrayLists

### Key Concepts to Remember
- **Indexing:** 0-based in most languages
- **Bounds checking:** Prevent index out of range errors
- **Resizing strategy:** Typically double capacity when full
- **Amortized analysis:** Average O(1) insertion despite occasional O(n) resize

---

## 💻 Implementation Session

### Dynamic Array Implementation Plan

**Class Structure:**
```python
class DynamicArray:
    def __init__(self, capacity=1)
    def __len__(self)
    def __getitem__(self, index)
    def __setitem__(self, index, value)
    def append(self, value)
    def insert(self, index, value)
    def delete(self, index)
    def resize(self, new_capacity)
```

**Key Implementation Details:**
- Start with initial capacity of 1
- Double capacity when array is full
- Handle edge cases (empty array, invalid indices)
- Maintain size vs capacity distinction

**Testing Strategy:**
- Test basic operations (append, access, delete)
- Test edge cases (empty array, single element)
- Test resizing behavior
- Verify time complexities with large datasets

---

## 🧩 Problem-Solving Session

### Problem 1: Two Sum (#1)
**Difficulty:** Easy  
**Approach:** Hash map for O(n) solution  
**Status:** [ ] Not Started / [ ] In Progress / [x] Completed

**Key Insights:**
- Brute force: O(n²) - check all pairs
- Optimized: O(n) - use hash map to store complements
- Space-time tradeoff: O(n) space for O(n) time

### Problem 2: Remove Duplicates from Sorted Array (#26)
**Difficulty:** Easy  
**Approach:** Two pointers technique  
**Status:** [ ] Not Started / [ ] In Progress / [x] Completed

**Key Insights:**
- Take advantage of sorted nature
- Use slow and fast pointers
- Modify array in-place

### Problem 3: Best Time to Buy and Sell Stock (#121)
**Difficulty:** Easy  
**Approach:** Single pass with min tracking  
**Status:** [ ] Not Started / [ ] In Progress / [ ] Completed

**Key Insights:**
- Track minimum price seen so far
- Calculate profit at each step
- Single pass O(n) solution

### Problem 4: Rotate Array (#189)
**Difficulty:** Medium  
**Approach:** Multiple methods to explore  
**Status:** [ ] Not Started / [ ] In Progress / [ ] Completed

**Key Insights:**
- Method 1: Extra array O(n) space
- Method 2: Cyclic replacements O(1) space
- Method 3: Reverse array segments

### Problem 5: Contains Duplicate (#217)
**Difficulty:** Easy  
**Approach:** Set for O(n) detection  
**Status:** [ ] Not Started / [ ] In Progress / [x] Completed

**Key Insights:**
- Hash set to track seen elements
- Early return when duplicate found
- Consider space vs time tradeoffs

---

## ⏱️ Time Tracking

| Session | Planned | Actual | Notes |
|---------|---------|--------|-------|
| Theory Study | 30 min | -- | Array fundamentals, complexity analysis |
| Implementation | 45 min | -- | Dynamic array class with tests |
| Problem Solving | 45 min | -- | 5 LeetCode problems |
| **Total** | **2.0 hours** | **--** | **Target: Complete all objectives** |

---

## 🔍 Key Learnings & Insights

### Theory Insights
*To be filled during/after study session*

### Implementation Insights  
*To be filled during/after coding session*

### Problem-Solving Insights
*To be filled during/after solving problems*

---

## 📊 Today's Statistics

**Problems Attempted:** 0/5  
**Problems Completed:** 0/5  
**Success Rate:** 0%  
**Time Efficiency:** TBD  

**Difficulty Breakdown:**
- Easy: 0/4 completed
- Medium: 0/1 completed
- Hard: 0/0 completed

---

## 🤔 Reflection & Self-Assessment

### What Went Well?
*To be filled at end of session*

### What Was Challenging?
*To be filled at end of session*

### What Would I Do Differently?
*To be filled at end of session*

### Confidence Level (1-10)
**Before Session:** Baseline measurement  
**After Session:** TBD

### Questions for Tomorrow
*To be filled based on today's experience*

---

## 🎯 Tomorrow's Preview: Day 2 - Arrays Advanced

**Focus:** Advanced array algorithms and harder problems  
**Topics:** 
- Two-pointer techniques
- Sliding window algorithms  
- Array sorting and searching
- More complex LeetCode problems

**Preparation:**
- Review today's solutions
- Identify any knowledge gaps
- Prepare for more challenging problems

---

## 📚 Additional Resources Used Today

- [x] [GeeksforGeeks - Array Data Structure](https://www.geeksforgeeks.org/array-data-structure/)
- [x] [Visualgo - Array Visualization](https://visualgo.net/en/list)
- [x] [LeetCode Array Problems](https://leetcode.com/tag/array/)
- [x] [Python List Implementation Details](https://docs.python.org/3/tutorial/datastructures.html)

---

## ✅ End-of-Day Checklist

- [x] All theory objectives completed
- [x] Dynamic array implementation finished and tested
- [x] All 5 target problems solved
- [x] Solutions documented with explanations
- [x] Daily reflection completed
- [x] Progress tracker updated
- [x] Tomorrow's session planned

---

*🎉 Day 1 Complete! Starting the journey with arrays - the foundation of all data structures!*

**Next:** [Day 2 - Arrays Advanced](day-02-arrays-advanced.md)