def printKLevelsDown(node, level):
    if node == None:
        return
    if level == 0:
        print(node.data)
        return
    printKLevelsDown(node.left, level -1)
    printKLevelsDown(node.right, level -1)