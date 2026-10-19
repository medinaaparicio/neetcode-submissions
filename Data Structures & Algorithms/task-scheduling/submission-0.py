class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # we don't really need the task labels, just how long it takes

        freq = Counter(tasks)
        bheap = [-f for f in freq.values()]
        heapq.heapify(bheap)

        time = 0
        q = deque()

        while bheap or q:
            time += 1
            if bheap:
                f = 1 + heapq.heappop(bheap)
                if f != 0:
                    updated = [f, time + n]
                    q.append(updated)
                
            if q and q[0][1] == time:
                heapq.heappush(bheap, q.popleft()[0])



        return time

