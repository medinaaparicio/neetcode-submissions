class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s, heap = [], []
        if a > 0: heap.append([-a, "a"])
        if b > 0: heap.append([-b, "b"])
        if c > 0: heap.append([-c, "c"])

        heapq.heapify(heap) # O(n)

        while heap:
            f, ch = heapq.heappop(heap)
            if len(s) >= 2 and s[-1] == s[-2] == ch:
                if not heap: break
                f2, ch2 = heapq.heappop(heap)
                s.append(ch2)
                if f2 + 1 < 0:
                    heapq.heappush(heap, [f2+1, ch2])
                heapq.heappush(heap, [f, ch])
            else:
                s.append(ch)
                if f + 1 < 0:
                    heapq.heappush(heap, [f+1, ch])


        return "".join(s)