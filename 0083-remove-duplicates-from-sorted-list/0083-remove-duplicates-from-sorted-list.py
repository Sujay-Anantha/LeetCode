# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Set to track unique values
        check = set()
        
        # Dummy node to simplify edge cases
        dummy = ListNode()
        current = dummy
        
        while head:
            # Check if the value of the current node has been seen
            if head.val in check:
                head = head.next
            else:
                # Add the value to the set and link the node
                check.add(head.val)
                current.next = head
                current = current.next  # Move current to the next node
                head = head.next
        
        # Break the connection to any remaining duplicate nodes
        current.next = None
        
        return dummy.next
#         check = []
#         dummy = Listnode()
#         current = dummy
#         while head:
#             if head is in check:
#                 head = head.next
#             else:
#                 check.append(head)
#                 current.next = head
#                 head = head.next
#             current = current.next
            
#         return dummy.next
            
        