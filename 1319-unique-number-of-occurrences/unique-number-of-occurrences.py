class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        occur = set()
        for f in freq.values():
            if f in occur:
                return False
            occur.add(f)
        return True