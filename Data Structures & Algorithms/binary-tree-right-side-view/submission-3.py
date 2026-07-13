# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        
        # BFS traversal, Queue
        q = collections.deque([root])
        while q:
            # the length represents the # of
            # nodes at a particular level
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                # attach the neighbors
                for n in [node.left, node.right]:
                    if n:
                        q.append(n)

                if i == qLen - 1: # the last node in queue
                    result.append(node.val)
        return result