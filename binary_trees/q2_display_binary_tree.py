# question 
# =========

# is similar to pre order traversal of the tree

# Binary Search Tree Structure

#        50
#      /    \
#    25      75
#   /  \    /  \
# 12   37  62  87
#     /      \
#    30       70

# output
# ========
# 25 <- 50 -> 75
# 12 <- 25 -> 37
# None <- 12 -> None
# 30 <- 37 -> None
# None <- 30  -> None
# 62 <- 75 -> 87
# None <- 62 -> 70
# None <- 70 -> None
# None <- 87 -> None

from q1_binary_tree_constructor import TreeConstructor, Node


def display_binary_tree(root):
	if root == None:
		return
	left_data = str(root.left.data) if root.left else "None"
	right_data = str(root.right.data) if root.right else "None"
	print(left_data + " <- " + str(root.data) + " -> " + right_data)
	display_binary_tree(root.left)
	display_binary_tree(root.right)


if __name__ == "__main__":
	array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
	root = TreeConstructor(array).driver()
	display_binary_tree(root)
