class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # success conditions sub arrays of size k , avg >= threshold
        successes = 0
        left, average = 0, 0
        nums = arr

        # for the first k-1 numbers
        # add them to what will become our average value
        # that way we mantain O(n)

        for right in range(len(nums)):
            # fetus window, only adding up to average
            if right < k - 1:
                average += nums[right]
            
            # once window is correct, calculate average
            if right - left == k - 1:
                average = (average + nums[right]) // k
                if average >= threshold: 
                    successes += 1
                average = (average * k) - nums[left]
                left += 1

        return successes







        