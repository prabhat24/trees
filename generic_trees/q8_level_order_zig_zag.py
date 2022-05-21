def level_zig_zag(root):
    st_patent = deque()
    st_child = deque()
    level = 0
    st_patent.append(root)
    while len(st_patent) + len(st_child) != 0:
        first_node = st_patent[-1]

        if level % 2 == 1: 
            for i in range(len(first_node.child)-1, -1, -1):
                st_child.append(first_node.child[i])
        else:
            for ch in first_node.child:
                st_child.append(ch)
        print(first_node.key, end=" ")
        st_patent.pop()
        if len(st_patent) == 0:
            st_patent = st_child
            st_child = deque()
            print()
            level += 1

