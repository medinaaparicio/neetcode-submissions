class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since heapify builds a min heap, let's negate the values
        # to build a max heap 
        if len(stones) == 1: return stones[0]
        maxHeap = [-stone for stone in stones] # O(n)
        heapq.heapify(maxHeap) # O(n), modifies in place!


        while len(maxHeap) > 1:
                
            x = - (heapq.heappop(maxHeap)) #O(1) ?
            y = - (heapq.heappop(maxHeap))#O(1) ?

            if x < y: stone = y - x
            elif y < x: stone = x - y
            else: continue

            heapq.heappush(maxHeap, -stone)
        
        if not maxHeap: return 0
        return -heapq.heappop(maxHeap)

        # cases to consider
        # two numbers of the same value
        # one single number
        # mix of positives and negatives
        # only the same numbers (even and odd)
        # sorted inc, dec ?

            


