class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootSet = set(dictionary)
        newSentence = []
        for word in sentence.split():
            for i in range(len(word)):
                if word[:i+1] in rootSet:
                    newSentence.append(word[:i+1])
                    break
            else:
                newSentence.append(word)
        return ' '.join(newSentence)