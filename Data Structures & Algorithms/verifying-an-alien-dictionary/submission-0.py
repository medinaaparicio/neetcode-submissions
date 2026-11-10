class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {char : i for i, char in enumerate(order)}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            mismatched = False
            for c1, c2 in zip(first, second):
                if ordering[c1] > ordering[c2]:
                    return False
                elif ordering[c1] < ordering[c2]:
                    mismatched = True
                    break
            if not mismatched and len(second) < len(first):
                return False
            
        return True
