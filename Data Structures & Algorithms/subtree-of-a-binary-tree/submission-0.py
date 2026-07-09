# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False

        # traverse tree, find node where root and Subroot value is the same, return isSameTree
        # only concern is that q does not state if tree can have duplicate values
        # so when result is true, return it, otherwise keep searching

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        
        # this is the recursive case, one of them is bound to be right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]):
        # !A!B + !(A)B + A!(B)
        if not a and not b:
            return True
        elif not a and b or a and not b:
            return False

        return a.val == b.val and self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)