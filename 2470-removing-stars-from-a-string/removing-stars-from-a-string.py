class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        for ch in s:
            stack.append(ch) if ch != '*' else stack.pop()
        return ''.join(list(stack))