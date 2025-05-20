# Blind75 Problem Solutions & Thought Process

This README contains my analysis of each Blind75 problem I’ve worked through, along with reflections on my thought process, struggles, and lessons learned.

---

## 1. **Contains Duplicate**
**Status:** ✅ Functional  
**Time Complexity:** O(n²)  

This solution works but is computationally inefficient. It checks each value against all others, which results in O(n²) time complexity.  
I plan to revisit this problem after gaining a better understanding of hashing. A hashing-based approach should reduce the time complexity to O(n).

---

## 2. **Remove Duplicates**
**Status:** ✅ Solved with Insight  

My main issue was trying to iterate over a list while simultaneously modifying it.  
It took me about 20 minutes to realize I should make a copy of the list for iteration and edit the original.  
**Lesson learned:** Never modify a data structure while reading from it — use a copy instead.

---

## 3. **Valid Anagram**
**Status:** ✅ Solved, then Simplified  

My initial solution was clunky. Later I realized the problem could be solved simply by sorting both strings and checking if they’re equal:

```python
return sorted(s) == sorted(t)
```

**Takeaway:** There’s usually a cleaner, more elegant way to solve a problem. It’s worth looking for it.

---

## 4. **Remove Element**
**Status:** ✅ Solved Easily  

This problem was straightforward. The key insight was to **ignore any elements that don’t contribute to the final result.**  
**Simplicity is powerful.**

---

## 5. **Concatenation of an Array**
**Status:** ✅ Solved  

This one was simple and direct. No additional notes.

---

## 6. **Reverse a Linked List**
**Status:** ✅ Solved with Struggles  

I struggled with how to return the result as `Optional[ListNode]`.  
After some Googling, I figured it out. What tripped me up was the need to initialize with:

```python
head = ListNode(...)
```

I got stuck trying to "remove" the first node, but then remembered I could just slice it out.  
**Reminder:** Fundamental tools like list slicing can often solve tricky problems.

---

## 7. **Merge Two Sorted Linked Lists**
**Status:** ✅ Solved After Fixing Edge Cases  

I initially forgot to handle the case when `l1` and `l2` had the same value, which led to an infinite loop.  
I also neglected to use a dummy node — without it, the return value was `None`.  
**Lesson learned:** Always account for **edge cases** and start with a solid structural setup like a dummy node.

---

## 8. **Maximum Subarray**
**Status:** ✅ Solved using Kadane’s Algorithm  

Kadane's Algorithm made this problem manageable.  
The key takeaway was maintaining **proper control flow** and tracking running totals smartly.

---

## Final Notes
This log helps me reflect on my learning process and reinforce lessons through practice. Each mistake is a step toward mastering these patterns.
