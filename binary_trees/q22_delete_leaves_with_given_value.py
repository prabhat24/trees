class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root, target: int):
        ans = self.helper(root, target)
        if ans:
            return None
        return root
        
    
    def helper(self, root, key):
        """
        returns True of node has to be removed as child
        false if nothing needs to be done
        """
        if root == None:
            return False
        
        lhs = self.helper(root.left, key)
        rhs = self.helper(root.right, key)

        if lhs:
            root.left = None
        if rhs:
            root.right = None
        # check if node is leaf node & data == key
        if root.val == key and root.left == None and root.right == None:
            # leaf node with data == key
            return True
        return False
        
