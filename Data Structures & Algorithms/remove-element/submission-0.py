class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        reader = writer = nonval = 0
        for num in nums: 
            if num != val: 
                nonval +=  1
                nums[writer] = nums[reader]
                writer += 1
            reader += 1
        return nonval


        