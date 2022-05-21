def issym_helper(node1, node2):
    if len(node1.child) != len(node2.child):
        return False
    for i in range(0, len(node1.child)):
        lr_child = node1.child[i]
        rl_child = node2.child[len(node2.child) -1 - i]
        ans = issym_helper(lr_child, rl_child) 
        if ans == False:
            return False
    return True

def issym(node):
    return issym_helper(node, node)