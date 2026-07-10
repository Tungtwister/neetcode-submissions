class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False

            if preReq[crs] == []:
                return True

            cycle.add(crs)

            for c in preReq[crs]:
                if dfs(c) == False:
                    return False
            
            cycle.remove(crs)
            preReq[crs] = []
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True
            
