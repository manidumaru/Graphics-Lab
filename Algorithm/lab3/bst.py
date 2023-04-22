from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.treeSize = 0
    
    def size(self):
        return self.treeSize

    def add(self, key, value):
        node = Node(key, value)

        if (self.root == None):
            self.root = node
            self.treeSize += 1
            print(f"{node.key}: root node added")
            return
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
                print(f"{node.key} added to left of {y.key}")
                return
            else:
                y.right = node
                self.treeSize += 1
                print(f"{node.key} added to right of {y.key}")
                return
    
    def smallest(self):
        if(self.root == None):
            print("tree is empty")
            return
        else:
            x = self.root
            while(x != None):
                y = x
                x = x.left
            result = (y.key, y.value)
            return result
    
    def largest(self):
        if(self.root == None):
            print("tree is empty")
            return
        else:
            x = self.root
            while(x != None):
                y = x
                x = x.right
            result = (y.key, y.value)
            return result
        
    def search(self, key):
        if (self.root == None):
            print("the tree is empty")
            return
        else:
            x = self.root
            while(x != None):
                if (x.key == key):
                    print(f"{key} found with value {x.value}")
                    return x.value
                elif(key < x.key):
                    x = x.left
                else:
                    x = x.right
        print(f"{key} not found")
        return False
    
    def inorder_walk(self):
        if (self.root == None):
            print("tree is empty")
            return
            


            

            
            
    

