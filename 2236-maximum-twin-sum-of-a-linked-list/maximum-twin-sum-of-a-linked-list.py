# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        maxTwin = 0
        for i in range(len(arr)//2):
            maxTwin = max(maxTwin, arr[i] + arr[-(i+1)])
        return maxTwin