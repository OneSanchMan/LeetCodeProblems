# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafSequence(root):
            q = []
            q.append(root)
            arr = []
            while q:
                node = q.pop()
                if not node.left and not node.right:
                    arr.append(node.val)
                else:
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
            return arr
        return getLeafSequence(root1) == getLeafSequence(root2)