"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = []
        for interval in intervals:
            meetings.append((interval.start, 1))
            meetings.append((interval.end, -1))
        
        meetings.sort()
        rooms = 0
        tobook = 0
        for time, active in meetings:
            rooms += active
            tobook = max(rooms, tobook)
        return tobook
