# code is similar to construct binary search tree from inorder traversal

# given array = [12, 25, 37, 50, 62, 75, 87]

from collections import deque

class TreeNode:
    
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

def construct_bst(arr, st, end):

    if st > end:
        return None

    mid = st + ((end - st) // 2)
    node = TreeNode(arr[mid])

    node.left = construct_bst(arr, st, mid-1)
    node.right = construct_bst(arr, mid+1, end)
    return node

def display_binary_tree(root):
	if root == None:
		return
	left_data = str(root.left.data) if root.left else "None"
	right_data = str(root.right.data) if root.right else "None"
	print(left_data + " <- " + str(root.data) + " -> " + right_data)
	display_binary_tree(root.left)
	display_binary_tree(root.right)

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


if __name__ == '__main__':
    array = [12, 25, 37, 50, 62, 75, 87]
    N = len(array)
    root = construct_bst(array, 0, N-1)

    display_level(root)




