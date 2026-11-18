
# Assessment 3.6: DFS Methods in Tree
# Name: Canag, Moises III R.
# Course: BSIT 2C

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the tree
root = Node("M")

root.left = Node("O")
root.right = Node("I")

root.left.left = Node("S")
root.left.right = Node("E")

root.right.left = Node("S")
root.right.right = Node("C")

root.left.left.left = Node("A")
root.left.left.right = Node("N")

root.left.right.left = Node("A")
root.left.right.right = Node("G")


# Preorder: Root, Left, Right
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Inorder: Left, Root, Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Postorder: Left, Right, Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Display the traversals
print("PREORDER:")
preorder(root)

print("\n\nINORDER:")
inorder(root)

print("\n\nPOSTORDER:")
postorder(root)
