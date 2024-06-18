class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(profit)
        pairs = [(difficulty[i], profit[i]) for i in range(n)]
        pairs.sort()
        res = 0
        max_profit = 0
        i = 0
        for w in sorted(worker):
            while i < n and w >= pairs[i][0]:
                max_profit = max(max_profit, pairs[i][1])
                i += 1
            res += max_profit
        return res