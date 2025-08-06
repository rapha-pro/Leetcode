class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        num_freq = {}
        buckets = [[]] * n
        output = []

        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)

        for key in nums:
            buckets[num_freq[key]] = key

        for i in range(n-1, 0, -1):
            for val in buckets[i]:
                output.append(val)
                if len(output) == k: return output
