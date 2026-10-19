class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # i'm thinking i can have a fast and slow pointer technique
        # where the slow pointer will potentially go through the whole list
        # fast = 0
        # for slow in range(len(nums)):
        #     if fast + 2 > len(nums) - 1:
        #         fast = (fast + 2) % len(nums) 
        #     else: 
        #         fast = fast + 2
        #     if nums[slow] == nums[fast]:
        #         return nums[slow]

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        # we're in the cycle! we just need to find the head now
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        # if we exited, we found the head and the duplicate!!
        return slow




        