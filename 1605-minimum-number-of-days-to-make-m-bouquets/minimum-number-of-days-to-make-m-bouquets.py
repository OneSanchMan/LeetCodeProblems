class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        l = min(bloomDay)
        r = max(bloomDay)
        ans = -1

        while l <= r:
            mid = (l + r) // 2
            bouquets = 0
            flowers = 0
            for b in bloomDay:
                if b <= mid:
                    flowers += 1
                    if flowers == k:
                        flowers = 0
                        bouquets += 1
                else:
                    flowers = 0
            if bouquets >= m:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans