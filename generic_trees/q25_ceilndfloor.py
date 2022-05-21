def ceilndfloor(node, data):
    global ceil, floor
    if node.data > data:
        ceil = min(ceil, node.data)
    elif node.data < data:
        floor = max(floor, node.data)
    for ch in node.child:
        ceilndfloor(ch, data)