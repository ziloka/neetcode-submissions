# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # must remove it recursively
        # function returns the next node
        # use global variable for the count
        # as you hit the end, increment by one
        # if equals n, return the next node

        count = 0
        def helper(node):
            if not node:
                return None

            node.next = helper(node.next)
            nonlocal count
            count += 1

            if count == n:
                return node.next
            else:
                return node

        return helper(head)