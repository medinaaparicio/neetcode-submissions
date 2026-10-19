class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        k = curr = 1
        prev = 0    

        while curr < len(nums):
            if nums[prev] == nums[curr]:
                curr += 1
            else: # if they are different
                k += 1 # update amt of unique nums
                nums[prev+1] = nums[curr]
                prev += 1
                curr += 1
        return k


        


        