class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} # val -> index

        for index, value in enumerate(nums):
            diff = target - value
            if diff in indices:
                return [indices[diff], index]
            indices[value] = index

        
