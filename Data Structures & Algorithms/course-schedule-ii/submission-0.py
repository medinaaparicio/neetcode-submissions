class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. create the adj list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, prereq in prerequisites:
            adj[course].append(prereq)


        # 2. define our dfs; which updates what classes we have already taken
        # and keeps track of our potential schedule
        schedule, taken = [], set()
        track = set()

        def dfs(course):
            if course in track:
                return False
            
            if course not in taken:
                taken.add(course)
                track.add(course)
                for prereq in adj[course]:
                    placed = dfs(prereq)
                    if not placed: return False
                track.remove(course)
                schedule.append(course)
            return True

        # 3. run that to explore all nodes in the graph
        # which means all courses we must take
        for course in range(numCourses):
            placed = dfs(course)
            if not placed: return []
        
        return schedule if len(taken) == numCourses else []