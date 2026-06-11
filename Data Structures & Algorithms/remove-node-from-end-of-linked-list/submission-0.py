# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # naive solution O(n) space
        # shove each listnode into a list, slice nth node off of list
        # and assign the n-1 node next to the new nth node

        # optimized O(1) space
        # recursion. why?
        # you traverse and you hit the end
        # now you need to rewind, return the link of the nodes
        # but you also need to keep track of n node from the end
        # so you know what node to remove
        # how would you do that? 
        # well since functions only have one return value
        # this makes a iterative approach better

        def helper(node: Optional[ListNode]):
            if node is None:
                return (node, 0)
            
            nextNode, last = helper(node.next)
            curr_dist = last+1

            if curr_dist == n:
                return (node.next, curr_dist)
            else:
                node.next = nextNode
                return (node, curr_dist)

        return helper(head)[0]