class Node:
    def __init__(self,data,left=None,right=None):
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


def createLeftCloneTree(node):
    if node == None:
        return Node

    createLeftCloneTree(node.left)
    createLeftCloneTree(node.right)
    cn = Node(node.data)
    cn.left = node.left
    node.left = cn
    return node

  
if __name__ == '__main__':

    n = int(input())
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
    root = createLeftCloneTree(root)
    display(root)