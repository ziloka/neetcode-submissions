# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # this has to be bottom-up DFS bc we must do validation
        # this question makes sense for perfect BST
        # but what about imperfect BST?
        # eg left node is 1, and right node is None?

        # def dfs(node):
        #     # base case
        #     if not node:
        #         return True

        #     # if children does not fit constraint, early exit
        #     if not dfs(node.left) or not dfs(node.right):
        #         return False

        #     # check if current node is not valid
        #     if node.left and node.right:
        #         return node.left.val < node.val and node.val < node.right.val
        #     elif node.left:
        #         return node.left.val < node.val
        #     elif node.right:
        #         return node.right.val > node.val
        #     else:
        #         return True

        # return dfs(root)

        # the solution above works mostly, except ... DFS must be
        # top down, because we need to worry about a node being
        # in the wrong subtree. aka check globally, not locally
        
        def dfs(node, low, high):
            # base case
            if not node:
                return True

            # check if current node is not valid
            if low > node.val or node.val > high: 
                return False

            # continue moving down the tree
            return dfs(node.left, low, node.val-1) and dfs(node.right, node.val+1, high)

        return dfs(root, float('-inf'), float('inf'))