class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for base in range(len(s)):
            res += 1 # single letter is always a palindrome 

            # grow odds, check left and right base 
            l, r = base - 1, base + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            # grow evens, 
            l, r = base, base + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res