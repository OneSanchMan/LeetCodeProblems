class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        for i in range(min(n, n), 0, -1):
            if (n % i == 0 and 
            m % i == 0 and 
            str1 == str1[:i] * (n // i) and 
            str2 == str1[:i] * (m // i) ):
                return str1[:i]
        return ""