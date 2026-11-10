"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # touching endpoints does not count as overlap
        meetings = []
        for interval in intervals:
            start, end = interval.start, interval.end
            meetings.append((start, 1))
            meetings.append((end, -1))
        
        meetings.sort()
        attending = 0 
        for time, active in meetings:
            attending += active
            if attending > 1:
                return False
        return True



