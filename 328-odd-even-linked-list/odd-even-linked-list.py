# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        oddHead = head
        odd = oddHead
        evenHead = head.next
        even = evenHead
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            try:
                even.next = odd.next
                even = even.next
            except:
                pass
        odd.next = evenHead
        return oddHead