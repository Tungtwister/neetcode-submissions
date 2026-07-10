class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0
        while l < r:
            height = min(heights[l],heights[r])
            width = r - l
            area = height * width
            max_water = max(area, max_water)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
            
        return max_water    