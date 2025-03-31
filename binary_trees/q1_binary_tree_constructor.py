# question
# ========== 
# construct a binary tree from a constructer array

# given array
# [50, 25, 12, null, null, 37, 30, null, null, null, 75, 62, null, 70, null, null, 87, null, null]


# Binary Search Tree Structure

#        50
#      /    \
#    25      75
#   /  \    /  \
# 12   37  62  87
#     /      \
#    30       70

from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeConstructor():
    
    def __init__(self, arr):
        self.itr = 0
        self.N = len(arr)
        self.arr = arr

    def createTree(self):
        if self.arr[self.itr] == None:
            return None
        n = Node(self.arr[self.itr])
        self.itr += 1
        n.left = self.createTree()
        self.itr += 1
        n.right = self.createTree()
        return n

    def driver(self):
        root = self.createTree()
        return root


    # this is just written to verify that tree is properly created
    @staticmethod
    def print_level_order(root):
        q = deque()
        q.append(root)
        q.append(None)

        while q:
            ele = q.popleft()

            if ele is None:
                print()
                if len(q) != 0:
                    q.append(None)
                continue
            # work
            print("|", ele.data, 
                    f"left-> {ele.left.data if ele.left else None}",
                    f"right {ele.right.data if ele.right else None}",
                    end="| ")
            # append all childrens
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)

            


if __name__ == "__main__":
    array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    sol = TreeConstructor(array)
    root = sol.driver()
    sol.print_level_order(root)
