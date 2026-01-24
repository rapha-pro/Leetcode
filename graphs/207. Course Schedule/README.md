# [Leetcode 207. Course Schedule][Link]

###### Medium  
#### Related to Topological Sort, Cycle Detection (Directed Graph)

## Problem
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`.  
Some courses have prerequisites, where `prerequisites[i] = [a, b]` means you must take course `b` before course `a`.

Return `true` if you can finish all courses. Otherwise, return `false`.

<ins>_Example 1_</ins>:

**Input**: numCourses = `2`, prerequisites = `[[1,0]]`  
**Output**: `true`  

**Explanation**:  
You can take course `0` first, then course `1`.

---

## Steps to Solve:
- Think of the problem as a **graph problem**:
  - Each course is a node.
  - A prerequisite relationship forms a **directed edge** from the prerequisite to the course that depends on it.
- The key idea is to check whether the graph contains a **cycle**:
  - If there is a cycle, you can never complete all courses.
  - If there is no cycle, all courses can be completed.

- **Build the graph**:
  - Use an adjacency list where each course points to the courses that depend on it.
  - Also keep an `indegree` array:
    - `indegree[i]` represents how many prerequisites course `i` still needs.

- **Start with courses that have no prerequisites**:
  - Any course with an indegree of `0` can be taken immediately.
  - Add all such courses to a queue.

- **Process courses using BFS (Topological Sort)**:
  - Take one course from the queue and mark it as completed.
  - For every course that depends on it:
    - Reduce its indegree by 1 (since one prerequisite has now been satisfied).
    - If its indegree becomes `0`, add it to the queue.

- **Final check**:
  - Count how many courses were completed.
  - If the number of completed courses equals `numCourses`, return `true`.
  - Otherwise, return `false` (this means a cycle exists, and some courses can never be completed).

**Why this works**:  
Topological sorting only works for **Directed Acyclic Graphs (DAGs)**.  
If a cycle exists, at least one course in the cycle will always have an unmet prerequisite, preventing completion.

---

## Complexity
- `n`: number of courses (`numCourses`)
- `p`: number of prerequisite pairs

### Time: __O(n + p)__
- Building the graph → O(p)
- Processing each course and prerequisite once using BFS → O(n + p)

### Space: __O(n + p)__
- Graph adjacency list → O(p)
- Indegree array and queue → O(n)



[Link]: https://leetcode.com/problems/course-schedule/description/
