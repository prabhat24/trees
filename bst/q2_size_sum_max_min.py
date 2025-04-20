# find size, sum, find, max
from collections import deque

class TreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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

    def size_sum(self, root):
        if root == None:
            return 0, 0
        lsize, lsum = self.size_sum(root.left)
        rsize, rsum = self.size_sum(root.right)
        return lsize + rsize + 1, lsum + rsum + root.data

    def min(self, root):
        while root.left:
            root = root.left
        return root.data
    
    def max(self, root):
        while root.right:
            root = root.right
        return root.data

    def find(self, root, key):
        if root == None:
            return None
        if key == root.data:
            return root
        if key > root.data:
            return self.find(root.right, key)
        elif key < root.data:
            return self.find(root.left, key)



if __name__ == '__main__':
    array = [12, 25, 37, 50, 62, 75, 87]
    N = len(array)
    root = construct_bst(array, 0, N-1)
    sol = Solution()
    size, sum = sol.size_sum(root)
    print("size-> ", size, "sum->", sum)
    print("min->", sol.min(root), "max->", sol.max(root))

    key = 75
    find_root = sol.find(root, key)
    if find_root:
        display_level(find_root)
    else:
        print(f"node {key} does not exist")