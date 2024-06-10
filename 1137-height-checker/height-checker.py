class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([heights[i] != sorted(heights)[i] for i in range(len(heights))])