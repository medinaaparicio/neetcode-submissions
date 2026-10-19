class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if len(nums) == 1: return nums[0]

        # there is rotation, binary search deflection point
        if nums[left] >= nums[right]:
            while left < right: 
                mid = left + (right - left) // 2
                # check where we at 

                if nums[left] < nums[mid]:
                    # mid is in left chunk
                    left = mid
                
                else:
                    # mid is in right chunk
                    right = mid
            return nums[right+1]

        else: 
            # otherwise, no rotation, return first num
            return nums[left]
        