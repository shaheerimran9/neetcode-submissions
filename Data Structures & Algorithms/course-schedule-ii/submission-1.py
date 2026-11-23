class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        q = deque()
        indegree = [0] * numCourses
        completed = 0

        # Graph: Pre-req -> courses
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            if prereq not in graph:
                graph[prereq] = []

            graph[prereq].append(course)
            indegree[course] += 1

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()
            completed += 1
            res.append(course)
            neighbors = graph[course]

            for c in neighbors:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        if completed != numCourses:
            return []
        return res
            