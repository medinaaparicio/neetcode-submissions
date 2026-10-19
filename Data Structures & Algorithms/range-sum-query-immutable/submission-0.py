class NumArray:

    def __init__(self, nums: List[int]):
        # precompute works, since we'll always have 1 array nums
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        # here we want to grab the prefix at right
        # and subtract everything below left
        prefRight = self.prefix[right]
        prefLeft = self.prefix[left - 1] if left > 0 else 0
        return prefRight - prefLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# goal sumRange: returns the sum of the elems of nums btwn left and right