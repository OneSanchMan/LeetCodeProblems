class Solution:
    def compress(self, chars: List[str]) -> int:
        curChar = ''
        i = 0
        while i < len(chars):
            curChar = chars[i]
            j = i
            while j < len(chars) and chars[j] == curChar:
                j += 1
            if j-i > 1:
                intCh = str(j-i)
                chars[i:j] = [curChar] + list(intCh)
                i += len(intCh)
            i += 1