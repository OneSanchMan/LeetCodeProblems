class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefProd = []
        curPref = 1
        sufProd = []
        curSuf = 1
        for num in nums[::-1]:
            sufProd.insert(0, curSuf)
            curSuf *= num
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = curPref
            curPref *= temp
            sufProd[i] *= nums[i]
        return sufProd