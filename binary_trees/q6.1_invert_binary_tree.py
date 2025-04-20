# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        return self.helper_nlr(root)

    # this will work (postorder)
    def helper_lrn(self, root):
        if root == None:
            return None
        
        left = self.helper_lrn(root.left)
        right = self.helper_lrn(root.right)
        root.left = right
        root.right = left
        return root

    # this will work (preorder)
    def helper_nlr(self, root):
        if root == None:
            return root
        root.left, root.right = root.right, root.left
        self.helper_nlr(root.left)
        self.helper_nlr(root.right)
        return root


    # this does not work b/c of lnr (inorder traversal)
    def helper_lnr(self, root):
        if root == None:
            return root
        self.helper_lnr(root.left)
        root.left, root.right = root.right, root.left
        self.helper_lnr(root.right)
        return root

    
