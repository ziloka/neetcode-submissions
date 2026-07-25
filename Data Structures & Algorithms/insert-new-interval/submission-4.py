class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals either touch or submerged with one
        # to the other
        # |----|     |----|   |----|      |--|
        #   |----| |----|      |--|      |----|
        
        # note that there can also be multiple intervals
        # that are overlapping too

        # non-overlap = the max of the starts > min of the ends
        # condition to stop
        # |---|   |-----|    |-----|    |--|   |--|  -> intervals
        #   |-----------------------------|          -> newInterval

        # what if the intervals never overlap?
        # |----|               |---|
        #           |-------| 

        result = []
        LEN = len(intervals)
        n_start, n_end = newInterval
        i = 0

        # Phase 1: Add all intervals that end before newInterval starts
        while i < LEN and intervals[i][1] < n_start:
            result.append(intervals[i])
            i += 1

        # Phase 2: Merge all overlapping/touching intervals
        while i < LEN and intervals[i][0] <= n_end:
            n_start = min(n_start, intervals[i][0])
            n_end = max(n_end, intervals[i][1])
            i += 1
            
        result.append([n_start, n_end])

        # Phase 3: Add all remaining intervals that start after newInterval ends
        while i < LEN:
            result.append(intervals[i])
            i += 1

        return result