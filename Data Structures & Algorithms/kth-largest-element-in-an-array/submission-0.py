class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # find kth largest is maxheap and then get the top one
        neg = [-n for n in nums]
        heapq.heapify(neg)
        
        while k > 0: 
            res = heapq.heappop(neg)
            k -= 1
        return -res