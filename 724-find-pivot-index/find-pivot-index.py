class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefSum = 0
        prefSumList = [0]
        for num in nums:
            prefSum += num
            prefSumList.append(prefSum)
        for i in range(len(nums)):
            if prefSumList[i] + prefSumList[i+1] == prefSum:
                return i
        return -1