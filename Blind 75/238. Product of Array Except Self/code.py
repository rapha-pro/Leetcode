class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, output = [1]*n, [1]*n, [1]*n  # since first elem of prefix and last elem of suffix is always 1

        # scan left to right to find prefix product
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        # scan right to left to find suffix product
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for j in range(n):
            output[j] = prefix[j] * suffix[j]

        return output

