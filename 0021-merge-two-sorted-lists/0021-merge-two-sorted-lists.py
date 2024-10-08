# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         # Initialize a dummy node
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one of the lists is exhausted, append the other list
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the merged list, starting from dummy's next node
        return dummy.next
        