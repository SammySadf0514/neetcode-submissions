# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def heigh(node):
            if not node:
                return 0

            left_h = heigh(node.left)
            right_h = heigh(node.right)

            if left_h is False or right_h is False:
                return False
            
            diff = left_h - right_h

            if diff < -1 or diff > 1:
                return False

            return 1 + max(left_h, right_h)

        return heigh(root) is not False