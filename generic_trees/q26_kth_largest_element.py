import math 
ceil = 1<<31
floor=(1<<31)
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


def ceilndfloor(node, data):
    global floor
    global ceil
    if node.data > data:
        if node.data < ceil:
            ceil = node.data
    
    if node.data < data:
        if node.data > floor:
            floor = node.data
            
    for child in node.child:
        ceilndfloor(child,data)

def kthlargest(node,k):
    global floor
    data = floor
    floor = -(1<<31)
    ceilndfloor(node, data)
    for i in range(1, k):
        data = floor
        floor = -(1<<31)
        ceilndfloor(node, data)
    return floor
    
    
# number of elements as input
n = int(input())
lst = []
lst = list(map(int, input().split()))
 

root = constructor(lst,n)  
k = int(input())
kth = kthlargest(root, k)
print(kth)