from typing import Optional

INT_MAX = (1<<32) - 1 

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1 * INT_MAX
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if root == None:
            return 0
        
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right), 0)
        node_sum = left + right + root.val
        self.ans = max(self.ans, node_sum)
        return max(left + root.val, right + root.val)