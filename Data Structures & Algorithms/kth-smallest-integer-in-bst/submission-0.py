# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # swing through tree bottom left up down the right branch via in-order traversal DFS
        # not post order because I dont need to know both left and right
        # but in the event that the tree has majority nodes on the right branch
        # i would need to traverse over there to find the right element
        # once you hit bottom left, return the
        # k element, use global variable to track rank
        # if both ranks are equal, short circuit and return k
        rank = 0
        result = 0
        def helper(node):
            if not node:
                return None

            helper(node.left)
            
            # only increment rank on the way up
            nonlocal rank
            nonlocal result
            rank += 1
            if k == rank:
                result = node.val

            helper(node.right)

            return node
        helper(root)
        return result