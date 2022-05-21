def display_binary_tree(root):
	if root == None:
		return
	left_data = str(root.left.data) if root.left else "O"
	right_data = str(root.right.data) if root.right else "0"
	print(left_data + "->" + root.data + "<-" + right_data)
	display_binary_tree(root.left)
	display_binary_tree(root.right)

