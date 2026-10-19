class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [node for node in range(n)]
        children = [1] * n

        def findParent(node):
            # empezamos siendo nuestro propio parent
            parent = node
            while parent != parents[parent]:
                parents[parent] = parents[parents[parent]] # path compression
                parent = parents[parent]
            return parent

        def union(node1, node2):
            p1, p2 = findParent(n1), findParent(n2)
            # if my parents are the same, nada
            if p1 == p2: return 0 #estamos dentro del mismo component

             # if my parents are different: unimos, parent and rank update
            if children[p1] > children[p2]:
                parents[p2] = p1
                children[p1] += children[p2]
            else:
                parents[p1] = p2
                children[p2] += children[p1]
            return 1


           
        components = n
        for n1, n2 in edges:
            components -= union(n1, n2)
        return components
            


            
