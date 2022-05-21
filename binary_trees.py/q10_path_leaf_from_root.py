def pathToLeafFromRoot( node , path , suma, lo , hi):
    if node.right == None and node.left == None:
        suma += node.data
        if suma >= lo and suma <= hi:
            path += " "+ str(node.data)
            print(path)
    if node.left != None:
        pathToLeafFromRoot(node.left, path+" "+str(node.data) if suma else str(node.data), suma+node.data, lo, hi)
    if node.right != None:
        pathToLeafFromRoot(node.right, path+" "+str(node.data) if suma else str(node.data), suma+node.data, lo, hi)
 