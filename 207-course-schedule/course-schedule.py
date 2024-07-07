class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash_prer = defaultdict(list)

        for el in prerequisites:
            if el[0] not in hash_prer:
               hash_prer[el[0]] = [el[1]] 
            else:
                hash_prer[el[0]].append(el[1])

        seen = set()

        def dfs(course):
            if not hash_prer[course]:
                return True
            
            if course in seen:
                return False

            seen.add(course)


            for pre in hash_prer[course]:
                if not dfs(pre): 
                    return False

            hash_prer[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
