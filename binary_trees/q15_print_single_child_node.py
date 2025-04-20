class Node:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

idx = 0

def construct(arr):
    global idx
    if idx == len(arr) or arr[idx] == -1:
        idx = idx+1
        return None
    node = Node(arr[idx],None,None)
    idx = idx+1
    node.left = construct(arr)
    node.right = construct(arr)
    return node



def display(node):
    if node:
        s = ""
        s += "." if node.left == None else str(node.left.data)
        s += " <- " + str(node.data) + " -> "
        s += "." if node.right == None else str(node.right.data)
        print(s)
        display(node.left)
        display(node.right)

def printSingleChildNodes(node,parent):
    # write your code here
    if node==None:
        return
    if parent!=None and parent.left==None and parent.right!=None:
        print(node.data)
    if parent!=None and parent.left!=None and parent.right==None:
        print(node.data)
    
    printSingleChildNodes(node.left,node)
    printSingleChildNodes(node.right,node)

if __name__ == '__main__':
    s = input()
    l = list(s.split(" "))
    arr = []
    for i in range(len(l)):
        if(l[i] == 'n'):
            arr.append(-1)
             
        elif(l[i] == 'n\r'):
            arr.append(-1)
             
        else:      
            arr.append(int(l[i]))
             
    root = construct(arr)
    display(root)
    printSingleChildNodes(root, None)

# node input construction is based on preorder traversal

# input 1
# ========
# 10 20 n n 40 50 n 30 60 n 70 n n n n 
# output 1
# =======    
# 50
# 30
# 60
# 70
    
# input 2
# 1 2 4 n n 5 n n 3 6 n n n 

# output 2
# 6    


