from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# code for construction of bst
def construct_bst(arr, st, end):
    if st > end:
        return None

    mid = st + ((end - st) // 2)
    node = TreeNode(arr[mid])

    node.left = construct_bst(arr, st, mid-1)
    node.right = construct_bst(arr, mid+1, end)
    return node

# code for displaying in level order
def display_level(node):
    q = deque()

    q.append(node)
    q.append(None)

    while len(q) != 0:
        first = q.popleft()
        if first:
            if first.left:
                q.append(first.left)
            if first.right:
                q.append(first.right)
            print(first.data, end=" ")
        else:
            print()
            if len(q) != 0:
                q.append(first)

class Solution:

    def print_range(self, root, low, high):
        if root == None:
            return None

        if root.val < low:
            self.print_range(root.right, low, high)

        if  low <= root.val <= high:
            self.print_range(root.left, low, high)

            print(root.val)

            self.print_range(root.right, low, high)

        elif root.val > high:
            self.print_range(root.left, low, high)
        






if __name__ == '__main__':
    array = [12, 25, 37, 50, 62, 75, 87]
    N = len(array)
    root = construct_bst(array, 0, N-1)
    sol = Solution()
    sol.print_range(root, 25, 88)
