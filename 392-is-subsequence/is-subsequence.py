class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i, j, n, m = 0, 0, len(s), len(t)
        while i < n and j < m:
            if t[j] == s[i]:
                i += 1
                if i == n:
                    return True
            j += 1
        return False