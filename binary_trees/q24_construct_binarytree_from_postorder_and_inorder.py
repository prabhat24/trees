# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        N = len(inorder)
        self.inorder = inorder
        self.postorder = postorder
        return self.helper(0, N-1, 0, N-1)


    
    def helper(self, inst, inend, postst, postend):
        if inst > inend or postst > postend:
            return None

        inorder_root_ind = self.inorder.index(self.postorder[postend])

        left_side_ele = inorder_root_ind - inst
        right_side_ele = inend - inorder_root_ind
        left = self.helper(inst, inorder_root_ind-1, postst, postst + left_side_ele - 1)
        right = self.helper(inorder_root_ind+1, inend, postend - right_side_ele, postend-1)
        node = TreeNode(self.postorder[postend])
        node.left = left
        node.right = right
        return node