# [Leetcode 15. 3Sum][Link]

###### Medium  
#### Related Problem
[Leetcode 1. Two Sum][related_1], \
[Leetcode 167. Two Sum II][related_2]

## Problem
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:  

- `i != j`, `i != k`, and `j != k`, and  
- `nums[i] + nums[j] + nums[k] == 0`.  

Notice that the solution set must not contain duplicate triplets.

<ins>_Example 1_</ins>:

**Input**: nums = `[-1,0,1,2,-1,-4]`  
**Output**: `[[-1,-1,2],[-1,0,1]]`  

**Explanation**:  
- Triplet `[-1, -1, 2]` sums to 0.  
- Triplet `[-1, 0, 1]` sums to 0.  
- No other unique triplets exist.

---

## Steps to Solve:
- **Sort the array first**.  
  Sorting helps us in two ways:  
  1. It makes it easier to avoid duplicates since equal numbers will be next to each other.  
  2. It allows us to use the two-pointer approach to efficiently find pairs.  

- **Iterate through the array** with an index `i` that fixes one number (let’s call it `a`).  
  - If `a` is greater than 0, we can stop immediately. Since the array is sorted, everything after will also be positive, and no three positive numbers can sum to 0.  
  - If `a` is the same as the previous number, we skip it to avoid generating the same triplet multiple times.  

- **Use two pointers to find the other two numbers**:  
  - One pointer (`left`) starts just after `i`.  
  - The other pointer (`right`) starts at the end of the array.  
  - Together with `a`, these three form a potential triplet.  

- **Check the sum of the three numbers**:  
  - If the sum is too small (less than 0), move the `left` pointer to the right to increase the sum.  
  - If the sum is too large (greater than 0), move the `right` pointer to the left to decrease the sum.  
  - If the sum is exactly 0, we’ve found a valid triplet. Add it to the result.  

- **Handle duplicates carefully**:  
  - After finding a valid triplet, move the `left` pointer forward.  
  - Skip over any repeated values so that we don’t add the same triplet again.  

- Continue this process until all numbers have been checked, and return the list of unique triplets.

---

## Complexity
- `n`: number of elements in the array `nums`

### Time: __O(n²)__
- Sorting the array → O(n log n)  
- Iterating through the array and using two pointers for each element → O(n²)  
- Total → O(n²)  

### Space: __O(1)__
- Sorting is usually done in-place.  
- Only extra space is the result list, which is not counted toward space complexity.  

[Link]: https://leetcode.com/problems/3sum/description/  
[related_1]: /Blind%2075/1.%20Two%20Sum
[related_2]: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
