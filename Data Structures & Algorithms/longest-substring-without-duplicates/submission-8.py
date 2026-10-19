class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length, l= 0, 0
        seen = set()

        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1
            length = max(length, r - l + 1)

        return length



        