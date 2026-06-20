# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # bottom up DFS
        # return value is the value to compare the current node
        # that is being traversed
        # HANDLE ONE NODE AT A TIME

        count = 0
        def dfs(node, prevVal):
            if not node:
                return

            if prevVal <= node.val:
                nonlocal count
                count += 1

            greatestSeen = max(prevVal, node.val)

            isLeft = dfs(node.left, greatestSeen)
            isRight = dfs(node.right, greatestSeen)
        dfs(root, root.val)
        return count