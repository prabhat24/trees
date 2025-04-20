# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder, postorder):
        self.preorder = preorder
        self.postorder = postorder
        N = len(preorder)
        return self.helper(0, N-1, 0, N-1)


    
    def helper(self, prest, preend, postst, postend):
        if prest > preend or postst > postend:
            return None
        node = TreeNode(self.preorder[prest])
        pre_order_idx = prest + 1
        if not (prest <= pre_order_idx <= preend):
            return node

        idx = self.postorder.index(self.preorder[pre_order_idx])
        lhs_ele = idx - postst + 1
        left = self.helper(prest+1, prest + lhs_ele, postst, idx)
        right = self.helper(prest + lhs_ele + 1, preend, idx+1, postend-1)
        node.left = left
        node.right = right
        return node        

