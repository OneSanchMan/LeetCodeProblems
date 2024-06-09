class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerNum = 0
        if n == 0:
            return True
        m = len(flowerbed)
        if m == 1 and flowerbed[0] == 0:
            flowerNum += 1
        elif m >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            flowerNum += 1
        for i in range(m-2):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                flowerbed[i+1] = 1
                flowerNum += 1
            if flowerNum == n:
                return True
        if m >= 2 and flowerbed[-2] == 0 and flowerbed[-1] == 0:
            flowerNum += 1
        return flowerNum >= n