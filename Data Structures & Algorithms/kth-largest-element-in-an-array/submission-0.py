class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        largest = heapq.nlargest(k, nums)
        heapq.heapify(largest)
        return heapq.heappop(largest)