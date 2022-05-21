from collections import deque


class Node:

	def __init__(self, data):
		self.data = data
		self.children = list()


class Tree:

	def __init__(self):
		self.root = None



	def insert(self, arr):
		st = deque()

		for ele in arr:
			if ele == -1:
				st.pop()
				continue
			else:
				new_node = Node(ele)
				if len(st) == 0:
					self.root = new_node
				else:
					parent_node = st[-1]
					parent_node.children.append(new_node)
				st.append(new_node)


	@staticmethod
	def display_helper(root):
		# display root node
		print(str(root.data) + " -> ", end="")
		for node in root.children:
			print(node.data, end=" ")
		print(".")

		# print other subtrees
		for node in root.children:
			Tree.display_helper(node)


	def display(self):
		self.display_helper(self.root)


if __name__ == '__main__':
	arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80, 110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1, -1]
	tree = Tree()
	tree.insert(arr)
	tree.display() 
