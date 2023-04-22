
from bst import BinarySearchTree

tree = BinarySearchTree()

tree.search(65)
print(f"size of tree = {tree.size()}")

tree.add(50, "mouse")
tree.add(56, "pen")
tree.add(53, "metal")
tree.add(26, "band")
tree.add(29, "jar")
tree.search(19)
tree.add(60, "sixty")
tree.add(19, "loop")

print(f"size of tree = {tree.size()}")
tree.search(19)
tree.search(53)