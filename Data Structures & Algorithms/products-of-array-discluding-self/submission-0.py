class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build prefix array
        pref = [1]
        for i in range(len(nums) - 1):
            pref.append(nums[i] * pref[-1])
            
        # build suffix array
        suf = [1]
        for i in range(len(nums) - 1, 0, -1):
            suf.append(nums[i] * suf[-1])

        # build solution
        sol = []
        for i in range(len(nums)):
            sol.append(pref[i] * suf[len(suf) - 1 - i])
        return sol

        