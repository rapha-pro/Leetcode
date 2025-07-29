# Daily Leetcode challenge

![Python](https://img.shields.io/badge/code-python-blue?logo=python&logoColor=white)
![Java](https://img.shields.io/badge/code-java-red?logo=java&logoColor=white)
![LeetCode](https://img.shields.io/badge/solved-LeetCode-yellow?logo=leetcode&logoColor=white)


Most problems would be solved in sequence of the structure provided by the [Leetcode Beginner's study guide](https://leetcode.com/explore/learn/card/the-leetcode-beginners-guide/692/challenge-problems/4421/)
<br />
 _`Java`_,  _`Python`_

## File Structure

Each problem lives in a folder named like so: `###. Problem Title`  
Inside each folder:

- `code.[py/java]`: Coding implementation of the solution
- `README.md`: Problem description and complexity analysis

### Inside each problem's README
**Each readme includes**:
- LeetCode link and problem number
- Difficulty level
- Example section
- Elaborated Steps solution
- Complexity analysis (Time & Space)




## Creating a new problem directory:
To quickly scaffold a new problem directory with boilerplate files, use the `create_leetcode_problem.py` automation script:

```python
python create_leetcode_problem.py <problem_name> <leetcode_problem_link>

E.g:
python create_leetcode_problem.py "412. FizzBuzz" https://leetcode.com/problems/fizz-buzz/description/
```

```mermaid
graph TD
    A[Understand the Problem] --> B[Choose Optimal Data Struct]
    B --> C[Design Algorithm]
    C --> D[Write Initial Solution]
    D --> E{Passes Basic Tests?}
    E -- No --> F[Optimize/Debug]
    E -- Yes --> G[Time & Space Complexity Analysis]
    F --> D
    G --> H[Submit & Verify]
