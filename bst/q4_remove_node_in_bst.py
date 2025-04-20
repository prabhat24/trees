# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def get_max(self, root):
        if root.right == None:
            return root.val
        
        if root.right:
            return self.get_max(root.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val == key:
            if root.left == None and root.right == None:
                # no child nodes
                return None
            if root.left and root.right == None:
                # only left child exists:
                return root.left
            if root.right and root.left == None:
                # only right child exists:
                return root.right
            
            else:
                # else both left and right exists
                max_val = self.get_max(root.left)
                max_node = TreeNode(max_val)
                lft = self.deleteNode(root.left, max_val)
                max_node.left = lft
                max_node.right = root.right
                return max_node
            
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        return root
        