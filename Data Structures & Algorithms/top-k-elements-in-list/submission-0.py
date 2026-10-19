class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first let's build a frequency 
        # so each "node" is going to be at tuple
        # i am thinking of using a heap 

        # so first let's build my lists
        # or i could create a dictionary first?
        # this is taking up more space

        # build frequency dictionary
        freq = {}
        for num in nums:
            if num not in freq: 
                freq[num] = 0
            freq[num] += 1
        
        maxheap = []
        for key,val in freq.items():
            maxheap.append([-val, key])
        heapq.heapify(maxheap)

        i, ans= 0, []
        while i < k:
            ans.append(heapq.heappop(maxheap)[-1]) 
            i += 1
        return ans




        

        