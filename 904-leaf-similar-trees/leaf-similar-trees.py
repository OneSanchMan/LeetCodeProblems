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
        arr1 = getLeafSequence(root1)
        arr2 = getLeafSequence(root2)
        return len(arr1) == len(arr2) and all([arr1[i] == arr2[i] for i in range(len(arr1))])