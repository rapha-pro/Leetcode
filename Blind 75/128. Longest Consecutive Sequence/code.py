class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_sequence = 0

        for n in nums:
            # check if n is the start of a sequence
            if (n - 1) not in numSet:
                # Length of current sequence
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest_sequence = max(longest_sequence, length)

        return longest_sequence
