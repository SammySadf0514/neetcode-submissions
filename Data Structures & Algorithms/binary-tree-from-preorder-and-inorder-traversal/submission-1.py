class Solution:
    def buildTree(self, preorder, inorder):

        if not preorder:
            return None

        root = TreeNode(preorder[0])

        idx = inorder.index(preorder[0])

        left_sbt = inorder[:idx]
        right_sbt = inorder[idx + 1:]

        left_preorder = preorder[1:1 + len(left_sbt)]
        right_preorder = preorder[1 + len(left_sbt):]

        root.left = self.buildTree(left_preorder, left_sbt)
        root.right = self.buildTree(right_preorder, right_sbt)

        return root