class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        sub, longest = s[0], 1
        for i in range(len(s)):
            # grow odds, start 
            l, r = i-1, i+1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest:
                    sub = s[l:r+1]
                    longest = r - l + 1
                l -= 1
                r += 1

            # grow evens, start from base pair
            l, r = i, i+1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest:
                    sub = s[l:r+1]
                    longest = r - l + 1
                l -= 1
                r += 1
        return sub