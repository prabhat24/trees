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
    return root
    

class Solution():
    
    def preOrder(self, root):
        # code here
        
        st = deque()
        st.append([root, 1])
        
        lst = []
        while st:
            top_ele, step = st.pop()
            
            if step == 1:
                lst.append(top_ele.data)
                st.append([top_ele, step + 1])
                if top_ele.left:
                    st.append([top_ele.left, 1])
                
            if step == 2:
                st.append([top_ele, step + 1])
                if top_ele.right:
                    st.append([top_ele.right, 1])
                    
            if step == 3:
                continue
        return lst
    
    def postOrder(self,node):
        # code here
        lst = []
        
        st = deque()
        
        st.append([node, 1])
        
        while st:
            ele, step = st.pop()
            
            if step == 1:
                st.append([ele, 2])
                if ele.left:
                    st.append([ele.left, 1])
            
            if step == 2:
                st.append([ele, 3])
                if ele.right:
                    st.append([ele.right, 1])
                
            if step == 3:
                lst.append(ele.data)
        return lst

    def inOrder(self, root):
        # code here
        st = deque()
        st.append([root, 1])
        
        lst = []
        while st:
            ele, step = st.pop()
            
            if step == 1:
                st.append([ele, step + 1])
                if ele.left:
                    st.append([ele.left, 1])
            
            if step == 2:
                lst.append(ele.data)
                st.append([ele, step + 1])
                if ele.right:
                    st.append([ele.right, 1])
                    
            if step == 3:
                continue
        return lst

    

n = int(input())
st = input()
arr = [0]*n
arr = list(map(int,st.replace("n","-1").split(" ")));


root = construct(arr)
sol = Solution()

print(sol.preOrder())
print(sol.inOrder())
print(sol.postOrder())
