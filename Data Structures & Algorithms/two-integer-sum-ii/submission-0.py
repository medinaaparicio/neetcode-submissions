class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left, right = 0, len(numbers) - 1

        while left < right:
            suma = numbers[left] + numbers[right]

            if suma > target:
                right -= 1
            elif suma < target:
                left += 1
            else:
                return [left+1, right+1]