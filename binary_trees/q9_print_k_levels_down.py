from q1_binary_tree_constructor import TreeConstructor, Node
from collections import deque

# sol1
def printKLevelsDown(node, level):
    if node == None:
        return
    if level == 0:
        print(node.data)
        return
    printKLevelsDown(node.left, level -1)
    printKLevelsDown(node.right, level -1)


# sol2 - based on rwa stategy
def level_order_sol(root, level):
    q = deque()
    q.append(root)
    q.append(None)
    cur_level = 0
    while q:
        ele = q.popleft()
        if ele is None:
            cur_level += 1
            if q:
                q.append(None)
            continue
        
        # work
        if cur_level == level:
            print(ele.data)
        
        if ele.left:
            q.append(ele.left)
        if ele.right:
            q.append(ele.right)
        


# Binary Search Tree Structure

#        50
#      /    \
#    25      75
#   /  \    /  \
# 12   37  62  87
#     /      \
#    30       70


if __name__ == "__main__":
    array = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62, None, 70, None, None, 87, None, None]
    root = TreeConstructor(array).driver()

    print("sol1 =>")
    printKLevelsDown(root, 2)

    print("sol2 =>")
    level_order_sol(root, 2)
	