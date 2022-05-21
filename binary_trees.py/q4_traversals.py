def traversals(root):
	if root == None:
		return
	print("root visit in preorder", root.data)
	traversals(root.lt)
	print("root visit in inorder", root.data)
	traversals(root.rt)
	print("root visit in postorder", root.data)

