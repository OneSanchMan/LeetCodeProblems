class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                equal = True
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        equal = False
                        break
                count += equal
        return count