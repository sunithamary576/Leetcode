# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to act as the start of the merged list
        dummy = ListNode()
        # Pointer to track the current tail of the merged list
        curr = dummy
        
        # Traverse both lists until one runs out
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # Move the tail pointer forward
            curr = curr.next
            
        # Append the remaining elements of whichever list is left over
        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2
            
        # The head of the merged list is the node after the dummy
        return dummy.next
