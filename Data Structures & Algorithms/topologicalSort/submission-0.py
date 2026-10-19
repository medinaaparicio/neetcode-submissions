class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # in this problem, u must be completed first 
        # u is the prereq, v is the course 

        # 1. create an adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        for prereq, course in edges:
            adj[course].append(prereq)
        
        # 2. i want to make something that keeps track of the nodes i've already checked
        # i'm assuming that the graph is a dag
        # i'll run post order dfs on each node to make sure the node gets added only after it's successors have been added
        visited = set()
        path = set()
        ordering = []

        def dfs(node):
            if node in path:
                return False # there is a cycle

            if node not in visited:
                # mark node as visited, visit its successors and add to the ordering
                visited.add(node)
                path.add(node)
                for prereq in adj[node]:
                    placed = dfs(prereq)
                    if not placed: return False
                ordering.append(node)
                path.remove(node)
            return True
        
        # 3. for each node in the graph, we must explore it 
        for node in range(n):
            placed = dfs(node)
            if not placed: return []
        
        return ordering
        


        
