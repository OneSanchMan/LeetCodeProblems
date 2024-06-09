class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curHeight = 0
        maxHeight = 0
        for dif in gain:
            curHeight += dif
            maxHeight = max(maxHeight, curHeight)
        return maxHeight