class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        freq = dict()
        for num in hand:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        #print(freq)
        for _ in range(n//groupSize):
            curMin = min(freq.keys())
            for i in range(groupSize):
                #print(curMin, i)
                try:
                    freq[curMin+i] -= 1
                except:
                    return False
                if freq[curMin+i] == 0:
                    freq.pop(curMin+i)
        return True
