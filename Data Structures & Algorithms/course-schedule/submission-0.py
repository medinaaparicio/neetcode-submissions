class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 1. create adj list
        # a -> b; such that we will run post order dfs and not need to reverse the toposort
        # can i assume it's a DAG ? i will assume so for now, later address it
        # how are courses that have no prereqs represented?
        # they wont be in our adj list right? so i should initialize them with an empty list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        schedule = []
        taken = set()
        track = set()
        # 1.5 define dfs
        def dfs(course):
            if course in track: 
                return False

            if course not in taken:
                taken.add(course)
                track.add(course)
                for prereq in adj[course]:
                    placed = dfs(prereq)
                    if not placed: return False
                schedule.append(course)
                track.remove(course)
            return True

        # 2. for each node, run dfs keeping track of who's been visited (what courses we have taken so far)
        
        for course in range(numCourses):
            placed = dfs(course)
            if not placed: return False
        return len(taken) == numCourses