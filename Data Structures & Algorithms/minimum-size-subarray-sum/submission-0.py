class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums) + 1
        left, window_sum = 0, 0

        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum >= target:
                length = min(length, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if length == len(nums) + 1 else length

        