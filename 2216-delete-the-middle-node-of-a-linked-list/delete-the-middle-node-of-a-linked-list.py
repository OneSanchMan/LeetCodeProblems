# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        node = head
        while node.next:
            node = node.next
            n += 1
        if n == 1:
            return None
        middle = n // 2
        node = head
        while middle > 1:
            node = node.next
            middle -= 1
        node.next = node.next.next
        return head