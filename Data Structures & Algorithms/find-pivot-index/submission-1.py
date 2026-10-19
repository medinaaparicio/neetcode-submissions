class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # build postfix sum array
        postfix = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] + nums[i+1]

        # track sumsofar
        prefix = 0
        for i in range(len(postfix)):
            if prefix == postfix[i]:
                return i
            prefix += nums[i]
        return -1


        