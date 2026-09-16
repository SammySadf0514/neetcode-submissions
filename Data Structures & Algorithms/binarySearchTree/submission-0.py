class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.right = None
        self.left = None


#BST solved iteratively


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
    

        # iterative solution

        tempNode = TreeNode(key, val)

        # check if tree is empty and immediately insert
        if not self.root:
            self.root = tempNode
        else:
            # tree is not empty must traverse the tree to get curr to the correct spot
            curr = self.root
            while curr is not None:
                if curr.left is not None and tempNode.key < curr.key:
                    curr = curr.left
                elif curr.right is not None and tempNode.key > curr.key:
                    curr = curr.right
                elif tempNode.key == curr.key:
                    curr.val = tempNode.val
                    return
                else:
                    break

            # Now we traversed the tree and curr is in the lowest position
            # now need to check and insert
            if tempNode.key < curr.key:
                curr.left = tempNode
            elif tempNode.key > curr.key:
                curr.right = tempNode

    def get(self, key: int) -> int:


        if self.root is None:
            return -1
        elif key == self.root.key:
            return self.root.val

        else:
            curr = self.root

            while curr is not None:
                if curr.left is not None and key < curr.key:
                    curr = curr.left
                elif curr.right is not None and key > curr.key:
                    curr = curr.right
                elif key == curr.key:
                    return curr.val
                else:
                    break
            return -1

    def getMin(self) -> int:

        if self.root is None:
            return -1

        curr = self.root

        while curr is not None:
            if curr.left is not None and curr.left.key < curr.key:
                curr = curr.left
            else:
                break

        return curr.val

    def getMax(self) -> int:
        if self.root is None:
            return -1
        else:
            curr = self.root
            while curr is not None:
                if curr.right is not None and curr.right.key > curr.key:
                    curr = curr.right
                else:
                    break
            return curr.val

    def remove(self, key: int) -> None:
        curr = self.root
        prev = None

        # First check if the key is
        # actually present in the BST.
        # the variable prev points to the
        # parent of the key to be deleted
        while curr != None and curr.key != key:
            prev = curr
            if key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        if curr == None:
            return self.root

        # Check if the node to be
        # deleted has atmost one child
        if curr.left == None or curr.right == None:
            # newCurr will replace
            # the node to be deleted.
            newCurr = None

            # if the left child does not exist.
            if curr.left == None:
                newCurr = curr.right
            else:
                newCurr = curr.left

            # check if the node to
            # be deleted is the root.
            if prev == None:
                self.root = newCurr
                return

            # Check if the node to be
            # deleted is prev's left or
            # right child and then
            # replace this with newCurr
            if curr == prev.left:
                prev.left = newCurr
            else:
                prev.right = newCurr

            

        # node to be deleted
        # has two children.
        else:
            p = None
            temp = None

            # Compute the inorder
            # successor of curr.
            temp = curr.right
            while temp.left != None:
                p = temp
                temp = temp.left

            # check if the parent of the
            # inorder successor is the root or not.
            # if it isn't, then make the left
            # child of its parent equal to the
            # inorder successor's right child.
            if p != None:
                p.left = temp.right

            else:
                # if the inorder successor was
                # the root, then make the right child
                # of the node to be deleted equal
                # to the right child of the inorder
                # successor.
                curr.right = temp.right

            curr.key = temp.key
            curr.val = temp.val

        

    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr is None:
            return None

    def getInorderKeys(self) -> List[int]:
        result = []
        stack = []

        curr = self.root

        # outer loop to traverse the tree and right when left is finished
        while curr is not None or len(stack) > 0:
            # inner loop to traverse the left side and push it onto the stack
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            # curr should be none and at the left most part of the tree
            # pop off the left value
            curr = stack.pop()
            result.append(curr.key)
            curr = curr.right

        return result