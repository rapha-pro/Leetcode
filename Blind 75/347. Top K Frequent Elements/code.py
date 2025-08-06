class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 1: return nums

        num_freq = {}
        buckets = [[] for _ in range(n + 1)]
        output = []

        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)

        for num, freq in num_freq.items():
            buckets[freq].append(num)

        for i in range(n, 0, -1):
            for val in buckets[i]:
                output.append(val)
                if len(output) == k: return output
