class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 1. intialize table; node, parent, rank | sike! i actually cant because i dont have n </3
        rank, parents = {}, {}

        def find_root(node):
            # mientras mi papa no sea su propio papa
            # mi papa se vuelve mi abuelo
            # y vuelvo y busco desde mi abuelo
            while node != parents[node]:
                grandparent = parents[parents[node]]
                parents[node] = grandparent
                node = grandparent
            return node

        # union will find both parents
        # compare their ranks
        # and attach the smallest rank to bigger rank, in an attempt to keep trees fairly balanced
        def union(parentu, parentv):
            # if one is smaller rank than the other attach (meaning the rank wont increase since it's
            # getting attached at the root and it was already bigger through some other branch)
            if rank[parentu] > rank[parentv]:
                parents[parentv] = parentu
            elif rank[parentu] < rank[parentv]:
                parents[parentu] = parentv
            else:
                parents[parentv] = parents[parentu]
                rank[parentu] += 1

        # going to go through all the edges 
        for u, v in edges:
            # initialize them here
            if u not in parents:
                parents[u] = u
                rank[u] = 0
            if v not in parents:
                parents[v] = v
                rank[v] = 0
            
            parentu, parentv = find_root(u), find_root(v)
            # if they already have the same parent, introducing this edge would cause a cycle
            if parentu == parentv:
                return [u, v]
            # union the parents!
            union(parentu, parentv)

            
        
       