class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        n1, n2 = [q, p] if p.val > q.val else [p, q]       
        return self.helper(root, n1, n2) 

    
    def helper(self, root, n1, n2):
        if root == None:
            return None

        if  root.val > n2.val:
            return self.helper(root.left, n1, n2)
        
        elif root.val < n1.val:
            return self.helper(root.right, n1, n2)
        
        elif  n1.val <= root.val <= n2.val:
            return root
        