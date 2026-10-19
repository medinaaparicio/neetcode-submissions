"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        events = []
        for employee in schedule:
            for interval in employee:
                start = interval.start
                end = interval.end
                events.append((start, 1))
                events.append((end, -1))
        events.sort(key=lambda event:(event[0], -event[1]))
        working = 0
        res = []
        free = False
        for time, delta in events:
            working += delta
            if working == 0:
                free = True
                break_start = time
            # break just ended
            if free and working > 0:
                break_end = time
                res.append(Interval(break_start, break_end))
                free = False
        return res






        