# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # seems like bottom-up DFS, to count longest path

        count = 0
        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            nonlocal count
            count = max(count, left_depth+right_depth)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return count
        # count = 0

        # stack = [(root, 0)]
        # visited = set()
        # while len(stack) != 0:
        #     node, c = stack.pop()

        #     if node not in visited:
        #         # visit node
        #         count = max(count, c)
                
        #     visited.add(node)
        #     for n in [node.left, node.right]:
        #         if n is not None:
        #             stack.append((n, c+1))
        
        # return count