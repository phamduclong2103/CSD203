class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    #def
    def isEmpty(self):
        return self.root is None
    #def
    def clear(self):
        self.root = []
    #def
    def searchX(self,x):
        curr = self.root
        while curr is not None:
            if x == curr.data:
                return True
            elif x < curr.data:
                if curr.left is not None:
                    curr = curr.left
                else:
                    return False
            elif x > curr.data:
                if curr.right is not None:
                    curr = curr.right
                else:
                    return False
                
    #def
    def insertX(self,x):
        new_node = TreeNode(x)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while curr is not None:
                if x < curr.data:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = new_node
                    
                        break
                elif x > curr.data:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = new_node
                        break
    #def
    def breadth(self):
        if self.root is None:
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data,end=' ')

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    #def
    def preorder(self, p):
        if p is None:
            return
        print(p.data, end=" ")
        self.preorder(p.left)
        self.preorder(p.right)  
    #def
    def postorder(self, p):
        if p is None:
            return
        self.postorder(p.left)
        self.postorder(p.right)
        print(p.data,end=" ")  
    #def
    def inorder(self, p):
        if p is None:
            return
        self.inorder(p.left)
        print(p.data,end=" ")
        self.inorder(p.right)
    #def
    def count(self):
        return self._count_helper(self.root)
    
    def _count_helper(self,node):
        if node is None:
            return 0
        return 1 + self._count_helper(node.left) + self._count_helper(node.right)
    #def
    def dele(self, x):
        if not self.searchX(x):
            return  # Node does not exist
        self.root = self._delete_helper(self.root, x)

    def _delete_helper(self, node, x):
        if node is None:
            return None
        if x < node.data:
            node.left = self._delete_helper(node.left, x)
        elif x > node.data:
            node.right = self._delete_helper(node.right, x)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_right = self._find_min(node.right)
                node.data = min_right.data
                node.right = self._delete_helper(node.right, min_right.data)
        return node
    #def
    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)
    def _find_min(self,node):
        while node.left is not None:
            node = node.left
        return node
    
    #def
    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root) 
    
    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node
    #def
    def sum(self):
        return self._sum_helper(self.root)
    
    def _sum_helper(self,node):
        if node is None:
            return 0
        return node.data + self._sum_helper(node.left) + self._sum_helper(node.right)
    #def
    def avg(self):
        node_count = self.count()
        if node_count == 0:
            return 0
        tree_sum = self.sum()
        return tree_sum / node_count
    #def
    def height(self):
        return self._height_helper(self.root)
    
    def _height_helper(self,node):
        if node is None:
            return -1
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        return max(left_height,right_height) + 1
    #def
    def cost_of_most_expensive_path(self):
        return self.cost_helper(self.root)
    
    def cost_helper(self,node):
        if node is None:
            return 0
        left_cost = node.data + self.cost_helper(node.left)
        right_cost = node.data + self.cost_helper(node.right)
        return max(left_cost,right_cost)
    #def
    def is_AVL(self):
        return self._is_AVL_helper(self.root)

    def _is_AVL_helper(self, node):
        if node is None:
            return True
        left_height = self._height_helper(node.left)
        right_height = self._height_helper(node.right)
        if abs(left_height - right_height) > 1:
            return False
        return self._is_AVL_helper(node.left) and self._is_AVL_helper(node.right)
    #def
    def is_heap(self):
        return self._is_heap_helper(self.root)
    
    def _is_heap_helper(self,node):
        if node is None:
            return True
        if node.left is not None and node.left.data > node.data:
            return False
        if node.right is not None and node.right.data > node.data:
            return False
        return self._is_heap_helper(node.left) and self._is_heap_helper(node.right)


# Testing the Binary Search Tree implementation
tree = BST()
# Test isEmpty()
print("Is tree empty?", tree.isEmpty())
# Test insert()
tree.insertX(5)
tree.insertX(3)
tree.insertX(7)
tree.insertX(1)
tree.insertX(4)
tree.insertX(6)
tree.insertX(8)
# Test breadth()
print("Breadth traversal:")
tree.breadth() 
# Test search()
print("\nSearch 4:", tree.searchX(4))  # Output: <__main__.TreeNode object at 0x...>
print("Search 9:", tree.searchX(9))  # Output: None
# Test preorder()
print("\nPreorder traversal:")
tree.preorder(tree.root)  # Output: 5 3 1 4 7 6 8
# Test postorder()
print("\npostorder traversal:")
tree.postorder(tree.root)  # Output: 1 4 3 6 8 7 5
# Test inorder()
print("\ninorder traversal:")
tree.inorder(tree.root)  # Output: 1 3 4 5 6 7 8
# Test count()
print("\nCount number of nodes:", tree.count())  # Output: 7
# Delete a node
tree.dele(3)
# Test breadth() after deletion
print("Breadth traversal after deletion:")
tree.breadth()  # Output: 5 4 7 1 6 8

# Find the maximum value in the tree
max_node = tree.find_max()
if max_node is not None:
    print("\nMaximum value:", max_node.data)
else:
    print("Tree is empty.")

# Find the minimum value in the tree
min_node = tree.find_min()
if min_node is not None:
    print("minimum value:", min_node.data)
else:
    print("Tree is empty.")
#Caculate sum of the tree
print("Sum of all values in the tree:", tree.sum())
#Caculate average of the tree
print("Average of all values in the tree:", tree.avg())

# Calculate the height of the tree
tree_height = tree.height()
print("Height of the tree:", tree_height)
# Calculate the cost of the most expensive path
cost = tree.cost_of_most_expensive_path()
print("Cost of the most expensive path:", cost)
# Check if the tree is AVL
is_avl = tree.is_AVL()
print(is_avl)  # Output: True
# Kiểm tra cây root có phải là heap hay không
print(tree.is_heap())  # Kết quả: True
