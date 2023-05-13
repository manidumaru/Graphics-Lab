from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.treeSize = 0
    
    def head(self):
        return self.root.value
    
    def size(self):
        return self.treeSize

    def add(self, key, value):
        node = Node(key, value)

        if (self.root == None):
            self.root = node
            self.treeSize += 1
            # print(f"{node.key}: root node added")
            return node
        else:
            x = self.root
            while(x != None):
                y = x
                if (node.key < x.key):
                    x = x.left
                else:
                    x = x.right
            if(node.key < y.key):
                y.left = node
                self.treeSize += 1
                # print(f"{node.key} added to left of {y.key}")
                return
            else:
                y.right = node
                self.treeSize += 1
                # print(f"{node.key} added to right of {y.key}")
                return
    
    def smallest(self):
        if(self.root == None):
            return -1
        else:
            x = self.root
            while(x != None):
                y = x
                x = x.left
            result = (y.key, y.value)
            return result
    
    def largest(self):
        if(self.root == None):
            return -1
        else:
            x = self.root
            while(x != None):
                y = x
                x = x.right
            result = (y.key, y.value)
            return result
        
    def search(self, key):
        if (self.root == None):
            return -1
        else:
            x = self.root
            while(x != None):
                if (x.key == key):
                    # print(f"{key} found with value {x.value}")
                    return x.value
                elif(key < x.key):
                    x = x.left
                else:
                    x = x.right
        # print(f"{key} not found")
        return False

    def inorder(self, walk, root):
        if root == None:
            return
        self.inorder(walk, root.left)
        walk.append(root.key)
        self.inorder(walk, root.right)

    def inorder_walk(self):
        walk = []
        self.inorder(walk, self.root)
        return walk
    
    def preorder_walk(self):
        walk = []
        self.preorder(walk, self.root)
        return walk
    
    def preorder(self, walk, root):
        if root == None:
            return
        walk.append(root.key)
        self.preorder(walk, root.left)
        self.preorder(walk, root.right)
    
    def postorder_walk(self):
        walk = []
        self.postorder(walk, self.root)
        return walk
    
    def postorder(self, walk, root):
        if root == None:
            return
        self.postorder(walk, root.left)
        self.postorder(walk, root.right)
        walk.append(root.key)

    def remove(self, key):
        x = self.search(key)
        if not x:
            # print("key not found to delete")
            return -1
        
        to_delete = self.root
        parent = None
        while(to_delete.key != key):
            parent = to_delete
            if(key < to_delete.key):
                to_delete = to_delete.left
            else:
                to_delete = to_delete.right

        if (to_delete.right == None and to_delete.left == None): ####################### if leaf node ##########################
            if parent.left == to_delete:
                parent.left = None
            else:
                parent.right = None
            self.treeSize -= 1
        
        if (to_delete.left == None and to_delete.right != None) or (to_delete.right == None and to_delete.left != None): ############## if one child ##################
            if (to_delete.left == None):
                to_replace = to_delete.right
                to_delete.right = None
            else:
                to_replace = to_delete.left
                to_delete.left = None
            to_delete.key = to_replace.key
            to_delete.value = to_replace.value
            self.treeSize -= 1
        
        if (to_delete.right != None and to_delete.left != None): ################## if two children ###########################
            to_replace = to_delete.left
            to_replace_parent = None
            if to_replace.right == None:
                to_delete.key = to_replace.key
                to_delete.value = to_replace.value
                to_delete.left = None
                self.treeSize -= 1
            else:    
                while(to_replace.right != None):
                    to_replace_parent = to_replace
                    to_replace = to_replace.right
                to_replace_parent.right = None
                to_delete.key = to_replace.key
                to_delete.value = to_replace.value            
                self.treeSize -= 1
            

 
            


            

            
            
    

