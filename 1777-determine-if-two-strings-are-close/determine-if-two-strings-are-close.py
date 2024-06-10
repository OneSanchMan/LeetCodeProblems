class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = Counter(word1)
        freqFreq1 = Counter(freq1.values())
        freq2 = Counter(word2)
        freqFreq2 = Counter(freq2.values())
        return set(word1) == set(word2) and all([freqFreq1[f]==freqFreq2[f] for f in freqFreq1.keys()])