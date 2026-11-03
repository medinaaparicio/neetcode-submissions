class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        check = set(nums)
        starters = []
        for n in nums:
            if n-1 not in check:
                starters.append(n)
        length = 1
        for starter in starters:
            run = 1
            while starter + run in check:
                run += 1
            length = max(length, run)
        return length
