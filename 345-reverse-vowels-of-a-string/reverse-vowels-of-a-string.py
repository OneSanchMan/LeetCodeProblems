class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i = 0
        j = len(s) - 1
        newS = list(s)
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                newS[i], newS[j] = newS[j], newS[i]
                i += 1
                j -=1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return ''.join(newS)