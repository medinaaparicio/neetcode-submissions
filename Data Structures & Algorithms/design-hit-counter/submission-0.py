from collections import deque
class HitCounter:

    def __init__(self):
        self.storage = deque()
        self.total = 0
    def hit(self, timestamp: int) -> None:
        if self.storage and self.storage[-1][0] == timestamp:
            self.storage[-1][-1] += 1
        else:
            self.storage.append([timestamp, 1])
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.storage and (timestamp - self.storage[0][0] >= 300):
            self.total -= self.storage[0][-1]
            self.storage.popleft()
        
        # return how many hits
        return self.total

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
