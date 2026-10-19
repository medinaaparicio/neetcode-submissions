class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        vals = [0, 0, 0]
        for num in nums:
            vals[num] += 1
        
        writer = 0
        for i in range(len(vals)):
            for _ in range(vals[i]):
                nums[writer] = i
                writer += 1
        return

        