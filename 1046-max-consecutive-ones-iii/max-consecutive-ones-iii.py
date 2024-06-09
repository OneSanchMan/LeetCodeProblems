class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        longest = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            longest = max(longest, right-left+1)
        return longest
