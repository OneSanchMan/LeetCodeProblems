class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        width = right
        maxArea = 0
        while left < right:
            maxArea = max(maxArea, width * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            width -= 1
        return maxArea