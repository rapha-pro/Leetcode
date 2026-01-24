from typing import List
from collections import defaultdict, deque



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Cycle Detection. Topological Sort

        # 1. Build the graph
        graph = defaultdict(list)

        # indegree[i] = #courses required to take course 'i'
        indegree = [0] * numCourses

        # prereq -> [course, ...]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # 2. Check first the courses with 0 prerequisites and add to queue

        courses_to_do = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                courses_to_do.append(course)

        # BFS for course cycle detection
        completed = 0
        while courses_to_do:
            course_completed = courses_to_do.popleft()

            completed += 1

            # update the prereq of its dependent courses. since you graduated from the course
            for dependent_course in graph[course_completed]:
                indegree[dependent_course] -= 1

                if indegree[dependent_course] == 0:
                    courses_to_do.append(dependent_course)

        return completed == numCourses
