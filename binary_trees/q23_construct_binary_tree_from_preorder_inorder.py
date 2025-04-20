class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        N = len(self.inorder)
        return self.helper(0, N-1, 0, N-1)

    def helper(self, pst, pend, ist, iend):
        if pst > pend or ist > iend:
            return None
        idx = self.inorder.index(self.preorder[pst])
        lse = idx - ist
        left = self.helper(pst+1, pst + lse, ist, idx - 1)
        right = self.helper(pst + lse + 1, pend, idx + 1, iend)
        node = TreeNode(self.preorder[pst])
        node.left = left
        node.right = right
        return node
    