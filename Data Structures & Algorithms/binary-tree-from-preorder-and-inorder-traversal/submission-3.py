class Solution:
    def buildTree(self, preorder, inorder):

        positions = {}

        for i in range(len(inorder)):
            positions[inorder[i]] = i

        def build(pre_start, in_start, in_end):

            if in_start > in_end:
                return None

            root_value = preorder[pre_start]
            root = TreeNode(root_value)

            idx = positions[root_value]

            left_size = idx - in_start

            root.left = build(pre_start + 1, in_start, idx - 1)

            root.right = build(pre_start + 1 + left_size, idx + 1, in_end)

            return root

        return build(0, 0, len(inorder) - 1)