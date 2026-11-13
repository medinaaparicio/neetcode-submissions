from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(s) < len(p): return result

        # a valid window will always be of size p, which if we are here there is at least one such window
        need = Counter(p)
        left, right = 0, len(p) - 1
        needed = len(p)

        for right, ch in enumerate(s):
            # add it to my window
            if ch in need:
                if need[ch] > 0:
                    needed -= 1
                need[ch] -= 1
            
            # if the window is too big we have to shrink it 
            window_size = right - left + 1
            if window_size > len(p):
                # kick out leftmost
                kicked = s[left]
                if kicked in need:
                    need[kicked] += 1
                    if need[kicked] > 0:
                        needed += 1
                left += 1

            # if we do not need anything we're good
            if needed == 0: result.append(left)
        return result                

      






