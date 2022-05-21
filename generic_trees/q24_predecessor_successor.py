# sol 1 using list

class Solution:

	lst = list()
	counter = 0
	ind = None
 
	def solve_helper(self, root, data):
		lst.append(root)
		if  root.data == data:
			ind = counter
		counter += 1
		for ch in root.children:
			solve_helper(root)

	def solve(self, root, data)
		self.solve_helper(root, data)
		if self.ind != 0:
			pre = self.lst[self.ind-1]
		else:
			pre = None
		if self.ind != len(lst) - 1:
			succ =  self.lst[self.ind+1]
		else:
			succ = None


# sol2 without list in O(1) space

class Solution:

	pre = None
	succ = None
	counter = 0
	state = 0
 
	def solve_helper(self, root, data):
		if root.data == data:
			state = 1
		if state == 0:
			pre = root.data
		elif state == 1:
			succ = root.data
			state = 2
		counter += 1
		for ch in root.children:
			solve_helper(root)

	def solve(self, root, data)
		self.solve_helper(root, data)
