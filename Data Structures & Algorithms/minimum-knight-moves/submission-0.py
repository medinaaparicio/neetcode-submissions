class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        goal = [abs(x), abs(y)]
        spots = deque([[0, 0]])
        if goal == spots[0]: return 0

        # directions
        NORTH = [(2, 1), (2, -1)]
        SOUTH = [(-2, 1), (-2, -1)]
        EAST = [(1, 2), (-1, 2)]
        WEST = [(1, -2), (-1, -2)]
        steps = NORTH + SOUTH + EAST + WEST
                
        visited = {(0, 0)}
        hops = 0

        while spots:
            level_size = len(spots)
            hops += 1
            for _ in range(level_size):
                curr_spot = spots.popleft()
                for step in steps:
                    newx, newy = curr_spot[0] + step[0], curr_spot[1] + step[1]
                    new_spot = [newx, newy]
                    if tuple(new_spot) in visited: continue
                    if new_spot == goal:
                        return hops
                    
                    if newx < -2 or newy < -2: continue
                    spots.append(new_spot)
                    visited.add(tuple(new_spot))
            

        