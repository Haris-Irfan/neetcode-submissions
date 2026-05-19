class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            h = (r - l) * min(heights[r], heights[l])
            if h > currMax:
                currMax = h
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

            
        
        return currMax
        