class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # declarative thinking
        # invariant: A course can only transition to VISITED after 
        # all of its prerequisites have already reached VISITED
        # the first course that needs to be taken
        # UNVISITED 0: we haven't found the prequisites for this course 
        # VISITING  1: find the prequisites of the current course
        # VISITED   2: we know the prequisites of this course

        # index is course: list is the prereqs
        deps = [[] for _ in range(numCourses)]
        for curr, prereq in prerequisites:
            deps[curr].append(prereq)

        states = [0] * numCourses
    
        def dfs(prereq):
            # some other course requires this course
            # while the current course requires the other one
            if states[prereq] == 1:
                return False
            # we know all of the prequisites of this course
            elif states[prereq] == 2:
                return True
            
            # we are visiting this node
            states[prereq] = 1

            # ensure prerequisites are resolved
            for course in deps[prereq]:
                if not dfs(course):
                    return False

            # all prereqs is resolved?
            # then we know the prequisites of this course
            states[prereq] = 2
            return True

        # figure out all the prequisites for all
        # courses
        for course in range(numCourses):
            if states[course] == 0:
                if not dfs(course):
                    return False
        return True

            
