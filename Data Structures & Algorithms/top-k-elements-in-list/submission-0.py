import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        heap = []
        for n, freq in count.items():
            heapq.heappush(heap, (freq, n))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]