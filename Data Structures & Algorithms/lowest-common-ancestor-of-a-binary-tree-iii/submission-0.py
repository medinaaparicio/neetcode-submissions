"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # calculate their depths
        depthp, depthq = 0, 0
        current = p
        while current.parent is not None:
            depthp += 1
            current = current.parent

        current = q
        while current.parent is not None:
            depthq += 1
            current = current.parent  
        
        # move the deepernode by the difference
        diff = depthp - depthq
        if diff > 0:
            for _ in range(diff):
                p = p.parent
        else:
            for _ in range(abs(diff)):
                q = q.parent
        
        # move them up together until they match 
        while p != q:
            p = p.parent
            q = q.parent
        
        # now they are together so start keeping track of min
        return p
            
