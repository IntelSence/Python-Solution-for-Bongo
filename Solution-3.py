class Tree_Node:
 
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
   
 
def lca(root, node1, node2):
      if not root:
         return None
      if root.data == node1 or root.data == node2:
         return root.data
      left = lca(root.left, node1, node2)
      right =lca(root.right, node1, node2)
      if right and left:
         return root.data
      return right or left
 
           
root = Tree_Node(1)
root.left = Tree_Node(2)
root.right = Tree_Node(3)
root.left.left = Tree_Node(4)
root.left.right = Tree_Node(5)
root.right.left = Tree_Node(6)
root.right.right = Tree_Node(7)
root.left.left.left = Tree_Node(8)
root.left.left.right = Tree_Node(9)
 
node1 = int(input())
node2 = int(input())
print(lca(root,node1,node2))

# Runtime and space complexity  both are O(n).