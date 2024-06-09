class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cumSum = 0
        prefixSum = []
        modFreq = {0: 1}
        for i in range(len(nums)):
            cumSum += nums[i]
            cumSum %= k
            prefixSum.append(cumSum)
            if cumSum not in modFreq:
                modFreq[cumSum] = 1
            else:
                modFreq[cumSum] += 1
        res = 0
        for freq in modFreq.values():
            res += (freq * (freq-1) // 2)
        return res
            