class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {num: i for i, num in enumerate(nums1)}
        ans = [-1] * len(nums1)

        mono = []
        for i in range(len(nums2)):
            elem = nums2[i]

            # vaciamos el stack primero hasta donde podamos
            while len(mono) > 0 and mono[-1] < elem:
                # if top is less than elem, place next greatest
                value = mono.pop()
                ansi = d[value]
                ans[ansi] = elem

            # si esta en nums1, lo anadimos al stack ya cuando no podamos sacar mas
            if elem in nums1:
                mono.append(elem)
        return ans

        