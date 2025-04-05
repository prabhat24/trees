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

# M1
# ===
    
def size(node):
    if node == None:
        return 0
    lf_size = size(node.left)
    rt_size = size(node.right)
    return lf_size + rt_size + 1
        
def suma(node):
    if node == None:
        return 0
    lf_sum = suma(node.left)
    rt_sum = suma(node.right)
    return lf_sum + rt_sum + node.data
        
        
def maximum(node):
    if node == None:
        return -(1<<31)
    lf_max = maximum(node.left)
    rt_max = maximum(node.right)
    return max(max(lf_max, rt_max), node.data) 
        
        
def height(node):
    if node == None:
        return -1
    lf_ht = height(node.left)
    rt_ht = height(node.right)
    return max(lf_ht, rt_ht) + 1


# M2
# ===

class SumSolution:
    
    def __init__(self):
        self.sum = 0
    
    def sumBT(self, node) -> int:
        # code here
        self.preorder(node)
        return self.sum
        
    def preorder(self, node):
        if node == None:
            return
        self.sum += node.data
        self.preorder(node.left)
        self.preorder(node.right)

class SizeSolution:
    
    def __init__(self):
        self.size = 0
    
    def getSize(self, node) -> int:
        # code here
        self.preorder(node)
        return self.size
        
    def preorder(self, node):
        if node == None:
            return
        self.size += 1
        self.preorder(node.left)
        self.preorder(node.right)

class HeightSolution:
    # max depth is same as height of the tree
    def __init__(self):
        self.height = 0

    def maxDepth(self, root) -> int:
        self.recursion(root, 1)
        return self.height
        
    def preorder(self, root, cur_height):
        if root == None:
            return None

        self.height = max(self.height, cur_height)
        # print(self.height)
        self.preorder(root.left, cur_height + 1)
        self.preorder(root.right, cur_height + 1)

n = int(input())
st = input()
arr = list(map(int,st.replace("n","-1").split(" ")));
root = construct(arr)
print(size(root))
print(suma(root))
print(maximum(root))
print(height(root))