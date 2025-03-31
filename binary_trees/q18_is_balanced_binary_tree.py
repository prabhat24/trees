def isbbt(root):
    if root == None:
        return [True, 0]
    lbool, lht = isbbt(root.left)
    rbool, rht = isbbt(root.right)
    if ((abs(lht - rht)) <= 1) and lbool and rbool:
        return [True, max(lht, rht) + 1]
    else:
        return [False, max(lht, rht) + 1]


def isbalance(node):
    ans, ht= isbbt(node)
    return ans