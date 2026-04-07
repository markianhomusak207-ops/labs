def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))

def print_tree(root):
    h = height(root)
    width = 2 ** h

    level_nodes = [root]

    for level in range(h):
        gap = width // (2 ** (level + 1))
        line = ""
        next_nodes = []

        for node in level_nodes:
            if node:
                line += " " * (gap - 1) + f"{node.value:2}" + " " * (gap - 1)
                next_nodes.append(node.left)
                next_nodes.append(node.right)
            else:
                line += " " * (gap * 2)
                next_nodes.append(None)
                next_nodes.append(None)

        print(line)

        if level < h - 1:
            arrows = ""
            for node in level_nodes:
                if node:
                    arrows += " " * (gap - 1) + "/ \\" + " " * (gap - 1)
                else:
                    arrows += " " * (gap * 2)
            print(arrows)

        level_nodes = next_nodes