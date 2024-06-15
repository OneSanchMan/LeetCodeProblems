class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pairs = [(capital[i], profits[i]) for i in range(n)]
        pairs.sort()
        i = 0
        heap = []
        for _ in range(k):
            while i < n and pairs[i][0] <= w:
                heapq.heappush(heap, -pairs[i][1])
                i += 1
            if not heap:
                break
            w -= heapq.heappop(heap)
        return w