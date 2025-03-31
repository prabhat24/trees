# approach 1

dia = -1
def diameter(node):
    global dia
    if node == None:
        return 0
    lfht = diameter(node.left)
    rtht = diameter(node.right)
    dia = max(lfht + rtht, dia)
    return max(lfht, rtht) + 1