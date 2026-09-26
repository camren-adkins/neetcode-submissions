class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        area = 0
        max = 0
        while i != j:
            if heights[i] - heights[j] > 0: # if left is taller
                vol = heights[j] * (j-i)
            else:
                vol = heights[i] * (j-i)
            if vol > area:
                area = vol
            if heights[i] < heights[j]:
                i = i+1
            else:
                j = j-1
        return area

