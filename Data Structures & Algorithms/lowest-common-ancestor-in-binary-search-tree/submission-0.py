# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # hint of the invariants held via a BFS
        # hint of a recursive DFS approach to solve problem 

        # find p and q, depending if the current node val is between p and q's val
        # you know to current node is LCA
        # if current node val leans in one direction
        # one of the nodes is LCA
        
        # dfs base and recursive case usually revolves around 
        # the height of the tree
        def dfs(node):
            # base cases
            if not node:
                return None

            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else:
                return node
         
        return dfs(root)