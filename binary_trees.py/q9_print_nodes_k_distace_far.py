def printKLevelDown(node,k):
    if k<0:
        return
    if node == None:
        return
    if k == 0:
        print(node.data)
        return
    printKLevelDown(node.left,k-1)
    printKLevelDown(node.right,k-1)

def printKNodesFar(node,data,k):

    if node == None:
        return 0
    if node.data == data:
        printKLevelDown(node, k)
        return 1
    
    x = printKNodesFar(node.left, data, k)
    if x == k:
        print(node.data)
    if x > 0:
        printKLevelDown(node.right, k-x-1)
        return x + 1

    x = printKNodesFar(node.right, data, k)
    if x == k:
        print(node.data)
    if x > 0:
        printKLevelDown(node.left, k-x-1)
        return x + 1
    return 0