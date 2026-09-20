class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = {}
        for left, right in prerequisites:
            if left not in prereq_map:
                prereq_map[left] = []
            prereq_map[left].append(right)

        visited = {}
        # visited_map = {}
        def dfs(curr_course: int):
            if curr_course in visited:
                return visited[curr_course]
            if curr_course not in prereq_map:
                return True
            res = True
            # visited.add(curr_course)
            visited[curr_course] = False
            for prerequisite in prereq_map[curr_course]:
                res = res and dfs(prerequisite)
            # visited.remove(curr_course)
            visited[curr_course] = res
            return res
        final_res = True
        for course in prereq_map:
            final_res = final_res and dfs(course)
        return final_res
            