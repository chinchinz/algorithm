# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head : return head
        even = head.next
        evenHead = head.next
        odd = head
        
        while odd.next and even.next:
            # print(odd.val, even.val)
            odd.next = odd.next.next
            odd = odd.next
            
            even.next = even.next.next
            even = even.next
        
        odd.next = evenHead
        return head