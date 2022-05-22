def Bst(node, low, high):
    if node == None:
        return True

    if node.data >= high or node.data <= low:
        return False

    lfans = Bst(node.left, low, node.data)
    rtans = Bst(node.right, node.data, high)

    if lfans and rtans:
        return True
    else:
        return False