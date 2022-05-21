import math
class Node:
    def __init__(self, key):
        self.data=key
        self.child=[]
        
def newNode(key):
    temp= Node(key)
    return temp
        
class Pair:
    def __init__(self,node,st):
        self.node=node;
        self.state=st

def construct(lst, n) :
    root = None
    stack=[]
    for i in range(0,n):
        if lst[i]==-1:
            stack.pop()
        else:
            t=Node(lst[i])
            if len(stack)>0:
                stack[-1].child.append(t)
            else:
                root=t
            stack.append(t)
    return root
    
dia=0;
def height(node):
    global dia
    if not node.child:
        return 1
    l_max = 0
    l2_max = 0 
    for ch in node.child:
        ht  = height(ch)
        if ht >= l_max:
            l2_max = l_max
            l_max = ht
        elif ht > l2_max:
            l2_max = ht
    dia = l_max + l2_max
    return l_max + 1
    
#write your code here
    
    
n=int(input())
values = list(map(str, input().split()))
arr=[0]*n
for i in range(0,n):
    if values[i]!="n":
        arr[i]=int(values[i])
    else:
        arr[i]=None
root=construct(arr,n)
height(root)
print(dia)