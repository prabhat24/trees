from collections import deque
class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = None
        self.right = None
class Pair:
    def __init__(self,node,state):
        self.node = node
        self.state = state

def construct(arr):
    root=Node(arr[0],None,None)
    rtp=Pair(root,1);
    
    st=[]
    st.append(rtp);
    
    idx=0;
    n = len(arr)
    while(len(st)>0):
        top=st[-1];
        if top.state==1:
            idx+=1
            st[-1].state+=1
            if(arr[idx]!=-1):
                top.node.left = Node(arr[idx], None, None);
                lp = Pair(top.node.left, 1);
                st.append(lp);
            else:
                top.node.left=None;
        elif top.state==2:
            idx+=1
            st[-1].state+=1
            if(arr[idx]!=-1):
                top.node.right =  Node(arr[idx], None, None);
                rp =  Pair(top.node.right, 1);
                st.append(rp);
            else:
                top.node.right=None;
        else:
            st.pop()
    return root;
    
    
    
def iterativePrePostInTraversal(node):

    st = deque()
    st.append([node, -1])

    preorder = [] 
    inorder = []
    postorder = []
    while len(st):
        try:
            n, state = st.pop()
            if state == -1:
                st.append([n, state+1])
                preorder.append(n.data)
                continue
            elif state == 0:
                st.append([n, state+1])
                if n.left:
                    st.append([n.left, -1])
                continue
            elif state == 1:
                st.append([n, state+1])
                inorder.append(n.data)
                continue
            elif state == 2:
                st.append([n, state+1])
                if n.right:
                    st.append([n.right, -1])
                continue
            elif state == 3:
                postorder.append(n.data)
                continue
        except Exception as e:
            print(e)
    for i in preorder:
        print(i, end=" ")
    print()
    for i in inorder:
        print(i, end=" ")
    print()
    for i in postorder:
        print(i, end=" ")
    print()



    
    

n = int(input())
st = input()
arr = [0]*n
arr = list(map(int,st.replace("n","-1").split(" ")));


root = construct(arr)
iterativePrePostInTraversal(root)