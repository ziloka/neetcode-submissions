class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # calculate frequencies
        freqs = {}
        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1

        # build the buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in freqs.items():
            buckets[f].append(n)

        # get the result
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res