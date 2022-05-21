from collections import deque
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
    
def IterativePreandPostOrder(node):
    st = deque()

    st.append([node, -1,])
    pre = []
    post = []
    while len(st):
        n, state = st[-1]
        if state == -1:
            pre.append(n.data)
            st.pop()
            st.append([n, state + 1])
            continue
        if state in range(0, len(n.child)):
            st.pop()
            st.append([n, state + 1])
            st.append([n.child[state], -1])
            continue
        if state > len(n.child)-1:
            post.append(n.data)
            st.pop()
            continue
    for i in pre:
        print(i, end=" ")
    print()

    for i in post:
        print(i, end=" ")
    print()



n=int(input())
values = list(map(str, input().split()))
arr=[0]*n
for i in range(0,n):
    if values[i]!="n":
        arr[i]=int(values[i])
    else:
        arr[i]=None
root=construct(arr,n)
IterativePreandPostOrder(root)