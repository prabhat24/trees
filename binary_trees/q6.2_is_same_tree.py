# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)
    
    def helper(self, p, q):
        if p == None and q == None:
            return True
        if q and p == None:
            return False
        if p and q == None:
            return False
        if p.val == q.val:
            left = self.helper(p.left, q.left)
            if left == False:
                return False
            right = self.helper(p.right, q.right)
            if right == False:
                return False
            return True
        else:
            return False