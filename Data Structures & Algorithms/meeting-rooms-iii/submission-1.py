class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort() # sorted by start time
        popular = {room: 0 for room in range(n)} # initialize, rooms have not been used
        free, busy = [room for room in range(n)], [] # initialized 2 heaps
        heapq.heapify(free)
        heapq.heapify(busy)

        for start, end in meetings:
            # moving finished rooms to free
            while busy and busy[0][0] <= start:
                oldEnd, room = heapq.heappop(busy)
                heapq.heappush(free, room)
        
            if free:
                room = heapq.heappop(free) # smallest room available
                heapq.heappush(busy, (end, room))
            else:
                # they either overlap, or it was free
                # if there is nothing free, that must mean that the rooms are in busy
                oldEnd, room = heapq.heappop(busy)
                newEndTime = abs(start - end) + oldEnd
                heapq.heappush(busy, (newEndTime, room))
            popular[room] += 1
        
        # get the smallest most popular room
        return max(range(n), key= lambda room: popular[room])
        

