def nodeToRootPath(node, data):
    if node == None:
        return []
    if node.data == data:
        return [node.data, ]
    
    a = nodeToRootPath(node.left, data)
    if a:
        a.append(node.data)
        return a
    b = nodeToRootPath(node.right, data)
    if b:
        b.append(node.data)
        return b
    return []
