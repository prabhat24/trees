import math

maxa = -(1<<32)
msumnode = 0
class Node:
     
    def __init__(self, data):
        self.data = data
        self.child = []
   
 # Utility function to create a new tree node
def newNode(data):   
    temp = Node(data)
    return temp
     
def constructor(lst,n):
    root = None
    stack = []
    for i in range(0,n):
        if lst[i]==-1:
            stack.pop()
        else:
            t= Node(lst[i])
            if len(stack) > 0:
                stack[-1].child.append(t)
                
            else:
                root=t
                
            stack.append(t)
    return root


def nodewithmaxsum(node):
    global maxa, msumnode
    if not node.child:
        if node.data > maxa:
            maxa = max(maxa, node.data)
            msumnode = node.data
        return node.data
    suma = 0
    for ch in node.child:
        sub_tree_sum = nodewithmaxsum(ch)
        suma += sub_tree_sum
    if  suma + node.data > maxa:
        maxa = max(maxa, suma + node.data)
        msumnode = node.data
    return suma + node.data

  
lst = []
# number of elements as input
n = int(input())

lst = list(map(int, input().split()))
 

root = constructor(lst,n)  
nodewithmaxsum(root)
print(str(msumnode) + "@" + str(maxa))