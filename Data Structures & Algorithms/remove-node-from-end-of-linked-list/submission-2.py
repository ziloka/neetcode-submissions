# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # keep track of how far each node is from the end of the linked list
        # requires post order traversal the end of linked list is reference point
        # (you need to traverse to the end of the linked list, before doing processing logic)
        # the recursive call deletes a node by returning the next node... thus skipping the current node

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