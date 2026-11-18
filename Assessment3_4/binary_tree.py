# Assessment 3.3: Non-Linear Data Structure
# Binary Tree using the letters of CANAG

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    """Breadth-First Search: visit nodes level by level."""
    if root is None:
        return []

    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return result


def dfs_preorder(root):
    """Depth-First Search (Preorder): Root, Left, Right."""
    if root is None:
        return []

    result = [root.value]
    result += dfs_preorder(root.left)
    result += dfs_preorder(root.right)
    return result


# Create the tree based on the assessment diagram:
#
#         C
#        / \
#       A   N
#      / \
#     A   G

root = Node("C")
root.left = Node("A")
root.right = Node("N")
root.left.left = Node("A")
root.left.right = Node("G")

print("BINARY TREE TRAVERSAL")
print("BFS:", " - ".join(bfs(root)))
print("DFS (Preorder):", " - ".join(dfs_preorder(root)))
