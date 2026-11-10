class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        edges = {}
        # initialize their edges
        for word in words:
            for ch in word:
                edges[ch] = []
        
        for i in range(len(words) - 1):
            a = words[i]
            b = words[i + 1]
            shorter = b if len(a) > len(b) else a
            allSame = True
            for j in range(len(shorter)):
                if a[j] != b[j]:
                    edges[a[j]].append(b[j])
                    allSame = False
                    break # no following character can contribute to knowing more
            # if we're here, all the letters were the same
            # need the prefix check right
            if allSame and len(b) < len(a): return ""

        # now we have adj list so we can do toposort, except i think i forgot how to
        ordering = []
        path = set()
        def dfs(node):
            if node in visited: return True
            path.add(node)
            for neighbor in edges[node]:
                if neighbor in path:
                    path.remove(neighbor)
                    return False
                if not dfs(neighbor):
                    return False
            visited.add(node)
            ordering.append(node)
            path.remove(node)
            return True

        visited  = set()
        for node in edges.keys():
            if not dfs(node):
                return ""
        return "".join(ordering[::-1])




