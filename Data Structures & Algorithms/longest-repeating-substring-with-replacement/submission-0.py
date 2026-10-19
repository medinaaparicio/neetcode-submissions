class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 0. initiate our pointers 
        l = 0
        freqs = {}
        length = 0
        
        # while window is valid
        # and the window is valid when len(window) - freqs[most frequent] <= k
        # move right pointer
        # as soon as window is invalid 
        # move left pointer and update freq dictionary
        # continously store the max length 

        # 1. go through each of the letters
        for r in range(len(s)):

            # 2. add the frequency of what's in the window
            if s[r] not in freqs:
                freqs[s[r]] = 0
            freqs[s[r]] += 1

            # 3. keep track of the longest valid window
            while (r-l+ 1 - max(freqs.values())) > k:
                freqs[s[l]] -= 1
                l += 1
            # capture max length so far
            length = max(length, r-l+ 1)
        return length


# 0123456
# AAABABB
# l
#     r

# A: 4, B: 1
# m = 4
# 1>1
# length = 5
# k = 1

            
            























        
        
        

        