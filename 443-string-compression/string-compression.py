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
                chars[i:j] = [curChar] + list(str(j-i))
                i += 1 + len(str(j-i))
            else:
                i += 1