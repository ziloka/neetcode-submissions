class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i, interval in enumerate(intervals):
            # Phase 1: Add all intervals that end before newInterval starts
            if interval[1] < newInterval[0]:
                result.append(interval)
            # Phase 3: Add all remaining intervals that start after newInterval ends
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            # Phase 2: Merge all overlapping/touching intervals
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        # If newInterval was never appended inside the loop (e.g., goes at the end)
        result.append(newInterval)
        return result