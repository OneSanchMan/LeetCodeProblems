class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        if k == 1:
            return True
        prefixSum = [nums[0]%k]
        for i in range(n-1):
            prefixSum.append((prefixSum[i]+nums[i+1]) % k)
        reminders = dict()
        for i in range(len(prefixSum)):
            r = prefixSum[i]
            if r == 0 and i > 0:
                return True
            if r in reminders:
                if reminders[r] < i-1:
                    return True
            else:
                reminders[r] = i
        return False