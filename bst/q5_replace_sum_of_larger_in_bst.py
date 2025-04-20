
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: 'TreeNode') -> TreeNode:
        self.agg = 0
        self.helper(root)
        return root

    def helper(self, root):

        if root == None:
            return None

        self.helper(root.right)
        self.agg += root.val
        root.val = self.agg
        self.helper(root.left)
        return