class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_l, max_r = heights[l], heights[r]
        max_area = 0
        while l < r:
            length = r - l

            area = min(heights[l], heights[r]) * length 

            if area > max_area:
                max_area = area
                max_l, max_r = l, r

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
