
from bst import BinarySearchTree

tree = BinarySearchTree()

tree.search(65)
print(f"size of tree = {tree.size()}")

root = tree.add(50, "fifty")
tree.add(23, "twenty three")
tree.add(80, "eighty")
tree.add(8, "eight")
tree.add(39, "thirty nine")
tree.add(98, "ninety eight")
tree.add(3, "three")
tree.add(13, "thirteen")
tree.add(28, "twenty right")
tree.add(44, "fourty four")


print(f"size of tree = {tree.size()}")
tree.search(19)
tree.search(53)

print(f"InOrder Walk = {tree.inorder_walk()}")
# print(f"PreOrder Walk = {tree.preorder_walk()}")
# print(f"PostOrder Walk = {tree.postorder_walk()}")

print(f"root is {tree.head()}")
tree.remove(50)
print(f"size of tree = {tree.size()}")
print(f"InOrder Walk = {tree.inorder_walk()}")
print(f"root is {tree.head()}")