class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for i in points:
            dist = ((i[0] - 0)**2 + (i[1] - 0)**2) ** 0.5
            closest.append((dist, i))
        heapq.heapify(closest)
        print(closest)
        res = []
        for i in range(k):
            distance, point= heapq.heappop(closest)
            res.append(point)
        return res