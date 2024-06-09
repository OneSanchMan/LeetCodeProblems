class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        freq = Counter(nums)
        for num in freq.keys():
            res += min(freq[num], freq[k-num])
        return res // 2