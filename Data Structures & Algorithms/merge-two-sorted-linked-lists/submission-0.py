# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # init head
        # while loop done when pointers for list1 and list2 are both at the end
        # check if both pointers are not None, and then check which is greater
        # if one pointer is None, then the next pointer is the other one
        # somehow return head at the end
        # good idea to use recursion

        # invariants: 
        # - two empty linked lists
        # - one empty, one not empty
        return self.helper(list1, list2)

    def helper(self, list1, list2):
        if list1 is None and list2 is None:
            return None

        if list1 is not None and list2 is not None:
            if list1.val < list2.val:
                list1.next = self.helper(list1.next, list2)
                return list1
            else:
                list2.next = self.helper(list1, list2.next)
                return list2
        else:
            # the rest of the nodes for the linked list are already sorted and attached
            return list2 if list1 is None else list1
    
        