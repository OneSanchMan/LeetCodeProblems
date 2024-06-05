class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        alph = "abcdefghijklmnopqrstuvwxyz"
        res = list()
        for ch in alph:
            minOccur = words[0].count(ch)
            for word in words:
                minOccur = min(minOccur, word.count(ch))
            res += [ch] * minOccur
        return res