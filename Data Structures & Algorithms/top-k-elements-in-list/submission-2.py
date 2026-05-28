class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, freq in count.items():
            buckets[freq].append(n)

        result = []
        for b in reversed(buckets):
            for n in b:
                result.append(n)
                if len(result) == k:
                    return result
        return result