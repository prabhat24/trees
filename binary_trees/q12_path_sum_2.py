
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from copy import deepcopy
from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        psf = []
        self.helper(root, psf, targetSum)
        return self.ans

    def helper(self, root, psf, target):
        if root == None:
            return None
        
        if root.left == None and root.right == None and root.val == target:
            psf.append(root.val)
            self.ans.append(list(psf))
            psf.pop()



        psf.append(root.val)
        self.helper(root.left, psf, target-root.val)
        self.helper(root.right, psf, target-root.val)
        psf.pop()