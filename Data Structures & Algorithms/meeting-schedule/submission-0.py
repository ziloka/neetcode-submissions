"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # use array, schedules. the intervals in them
        # either expand, or a new element is added for every Interval

        # conflict with interval
        # means that at least one of the start/end times
        # is between the other interval

        # for each interval
        # look in schedules, and see if the interval overlaps with any of them
        # if schedule conflicts with interval, cannot attend meetings
        # otherwise keep the intervals
        # finished, then can attend meetings
        # O(n^2) time, O(n) space
        # but if you sort it, you only need to check adjecent intervals
        intervals.sort(key=lambda a: a.start)

        for i in range(1, len(intervals)):
            prev = intervals[i - 1]
            curr = intervals[i]
            # so now the only case is if curr start time < prev end time
            if curr.start < prev.end:
                return False
        return True