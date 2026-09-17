# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], subRoot: Optional[TreeNode], flag: bool) -> bool:
            if subRoot is None:
                return root is None
            if root is None:
                return False
            if root.val != subRoot.val:
                if not flag:
                    return False
                return helper(root.left, subRoot, True) or helper(root.right, subRoot, True)
            else:
                return (helper(root.left, subRoot.left, False) and helper(root.right, subRoot.right, False)) or (helper(root.left, subRoot, True) or helper(root.right, subRoot, True))
        return helper(root, subRoot, True)
