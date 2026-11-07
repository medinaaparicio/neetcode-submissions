class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # keep prefix sums
        # si yo puedo restar algo que ya vi, de todo lo acumulado
        # LAS VECES QUE ESA SUMA APAREZCA son las veces que puedes hacer ese subarray

        counts = {0: 1}

        pref, result = 0, 0
        for n in nums:
            # 1. calculate new prefix sum 
            pref += n
            # 2. can we chop off a subarray to make k, if so inc res
            if pref - k in counts:
                result += counts[pref-k]

            # 3. update this new prefix we saw
            if pref not in counts:
                counts[pref] = 0
            counts[pref] += 1
        return result