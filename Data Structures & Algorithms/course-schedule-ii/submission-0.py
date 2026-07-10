class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit = set()
        visiting = set()
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visit:
                return True
            
            visiting.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
                
            visiting.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return output