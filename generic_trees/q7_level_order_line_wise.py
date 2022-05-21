
# using null to distinguish levels
def level_order_linewise(root):
    q = deque()
    # enqueue root
    # enqueue null
    q.append(root)
    q.append(None)

    while len(q)!=0:
        first_node = q[0]
        if first_node is None:
            print()
            q.popleft()
            if len(q) != 0:
                q.append(None)
        else:
            for ch in first_node.children:
                q.append(ch)
            print(first_node.key, end=" ")
            q.popleft()
        


# using 2 queues
def level_order_linewise_m2(root):
    # maintain children and parent q
    q_child = deque()
    q_parent = deque()


    # push first node to parent q
    q_parent.append(root)

    # iterate over patent q
    while len(q_child) + len(q_parent) != 0:
        first_node = q_parent[0]
        for ch in first_node.children:
            q_child.append(ch)
        print(first_node.key, end=" ")
        q_parent.popleft()
        
        if len(q_parent) == 0:
            q_parent = q_child
            q_child = deque()
            print()