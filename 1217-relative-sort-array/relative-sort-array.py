class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []
        for num in arr2:
            for _ in range(freq[num]):
                res.append(num)
            freq[num] = 0
        for num in sorted(freq.keys()):
            for _ in range(freq[num]):
                res.append(num)
        return res