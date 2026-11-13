class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3: return max(nums)
        prev2 = 0
        prev1 = 0
        for n in nums[1:]:
            rob = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = rob
        run1 = prev1
        prev2 = 0
        prev1 = 0
        for n in nums[:-1]:
            rob = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = rob
        run2 = prev1
        
        return max(run1, run2)
    

        