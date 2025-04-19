# given inorder traversal

# inorder = [9, 12, 14, 17, 19, 23, 50, 54, 67, 72, 76]


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def construct_bst(inorder):
    N = len(inorder)
    st = 0
    end = N -  1
    return helper(st, end, inorder)

def helper(st, end, inorder):

    if st > end:
        return None

    mid = st + ((end-st)//2)
    print(st, end, mid)
    left = helper(st, mid-1, inorder)
    right = helper(mid+1, end, inorder)
    node = Node(inorder[mid])
    node.left = left
    node.right = right
    return node

def display_binary_tree(root):
	if root == None:
		return
	left_data = str(root.left.data) if root.left else "None"
	right_data = str(root.right.data) if root.right else "None"
	print(left_data + " <- " + str(root.data) + " -> " + right_data)
	display_binary_tree(root.left)
	display_binary_tree(root.right)

if __name__ == '__main__':
    inorder = [9, 12, 14, 17, 19, 23, 50, 54, 67, 72, 76]
    root = construct_bst(inorder)
    display_binary_tree(root)

