class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prims algorithm
        # 1. start at any point
        # 2. add the distance of it to its neighbors and put it in a heap
        # 2.5 in this case, all neighbors not in the explored set are available
        # -- so we may go through the list of points, and if not in the visited set already, calculate their distance and 
        # 3. add that point to the visited set (to avoid cycles)
        # 4. stop when all nodes have been visited 
        tpoints = [tuple(p) for p in points]
        visited = set()
        heap = [(0, tpoints[0][0], tpoints[0][1])]
        curr = [0, 0]
        total = 0
        while len(visited) < len(points):
            dist, x, y = heapq.heappop(heap)
            if (x, y) in visited: continue # must skip the stale copy
            total += dist
            visited.add((x, y))
            for x1, y1 in tpoints:
                if (x1, y1) not in visited:
                    distance = abs(x - x1) + abs(y - y1)
                    heapq.heappush(heap, (distance, x1, y1))
        return total
