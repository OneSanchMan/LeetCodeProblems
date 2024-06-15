class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        new_sum = 0
        cur_max = -1
        for num in sorted(freq.keys()):
            print(num, freq[num])
            if cur_max < num:
                new_sum += (freq[num]-1)*freq[num] // 2
                cur_max = num + freq[num] - 1
            else:
                new_sum += (freq[num]+1)*freq[num] // 2 + (cur_max - num) * freq[num]
                cur_max = cur_max + freq[num]

        return new_sum