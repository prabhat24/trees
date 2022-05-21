def LevelOrderTraversal(root):
    q = deque()
    q.append(root)

    while len(q)!=0:
        first_node = q[0]
        
        # append
        for ch in first_node.child:
            q.append(ch)

        # print
        print(first_node.key, end=" ")

        # remove
        q.popleft()
    print(".")
    return