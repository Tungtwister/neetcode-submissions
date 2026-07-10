class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = {c : [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            preReq[crs].append(pre)

        
        cycle = set()
        visit = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True

            cycle.add(crs)

            for c in preReq[crs]:
                if dfs(c) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        

        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return output
