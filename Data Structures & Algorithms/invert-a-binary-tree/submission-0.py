# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(curr: Optional[TreeNode]):
            if not curr:
                return
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            helper(curr.left)
            helper(curr.right)
        helper(root)
        return root