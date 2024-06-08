class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        cur_rem = 0
        remainders = {0 : -1}
        for i in range(len(nums)):
            cur_rem = (cur_rem + nums[i]) % k
            if cur_rem in remainders:
                if remainders[cur_rem] < i-1:
                    return True
            else:
                remainders[cur_rem] = i
        print(remainders)
        return False