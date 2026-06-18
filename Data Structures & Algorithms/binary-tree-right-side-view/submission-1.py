# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # this seems like modified BFS
        # almost like BST level order traversal
        result = []

        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    if i == qLen - 1:
                        result.append(node.val)
                    for e in [node.left, node.right]:
                        if e:
                            q.append(e)
            
        return result