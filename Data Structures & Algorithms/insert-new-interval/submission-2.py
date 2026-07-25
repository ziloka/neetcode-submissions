class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # there are three basic overlap cases
        # end of first > start of second
        # start of first < end of the second
        # one interval completely overlaps the other

        # optimized solution O(n), space O(n)
        # you can merge intervals in a single pass
        # three un-nested loops
        # 1. append n elements until overlapping
        # 2. skip n elements until not overlapping
        # merge interval in result
        # 3. append rest of elements to result

        # intervals either touch or submerged with one
        # to the other
        # |----|     |----|   |----|      |--|
        #   |----| |----|      |--|      |----|
        
        # note that there can also be multiple intervals
        # that are overlapping too
        # |---|   |-----|    |-----|    |--|   -> intervals
        #   |-----------------------------|    -> newInterval

        # non-overlap = the max of the starts > min of the ends
        # condition to stop
        # |---|   |-----|    |-----|    |--|   |--|  -> intervals
        #   |-----------------------------|          -> newInterval

        # what if the intervals never overlap?
        # |----|               |---|
        #           |-------| 

        if len(intervals) == 0:
            return [newInterval]

        result = []
        LEN = len(intervals)

        n_start, n_end = newInterval
        i = 0
        # append n elements until interval end >= newInterval's start,
        # or end of list
        while i < LEN and intervals[i][1] < n_start:
            result.append(intervals[i])
            i += 1

        # there is never a overlap, append to end of list
        # or one interval in the intervals array
        if i >= LEN:
            return [*result, newInterval]

        # skip merged intervals
        while i < LEN and intervals[i][0] <= n_end:
            start, end = intervals[i]
            n_start = min(n_start, intervals[i][0])
            n_end = max(n_end, intervals[i][1])
            i += 1
        # place interval correctly
        result.append([n_start, n_end])
        
        # place rest of intervals
        while i < LEN:
            result.append(intervals[i])
            i += 1

        return result
