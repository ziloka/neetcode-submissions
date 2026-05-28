class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        rank = sorted(count.items(), key=lambda e: e[1], reverse=True)[:k]
        return [e[0] for e in rank]