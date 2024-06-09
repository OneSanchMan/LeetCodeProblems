class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = nums[0] #current minimum element
        second = None #Always greater than first
        for i in range(1, len(nums)):
            if nums[i] < first:
                first = nums[i]
            elif second is None and nums[i] > first:
                second = nums[i]
            elif second is not None and nums[i] > first and nums[i] < second:
                second = nums[i]
            elif nums[i] > first and nums[i] > second:
                return True
        return False