# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])

        idx = inorder.index(preorder[0])

        left_sbt = inorder[:idx]
        right_sbt = inorder[idx + 1:]

        left_preorder = preorder[1 : 1 + len(left_sbt)]
        right_preorder = preorder[1 + len(left_sbt):]

        root.left = self.buildTree(left_preorder, left_sbt)
        root.right = self.buildTree(right_preorder, right_sbt)

        return root