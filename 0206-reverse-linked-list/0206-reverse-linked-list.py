# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev up by one
            current = next_node  # Move current up by one
            
        return prev