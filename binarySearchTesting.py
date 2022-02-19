class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


class PreOrderSolution:
    def traverse(self, node, values):

        if node == None:
            return 
        
        values.append(node.val)

        if node.left != None:
            self.traverse(node.left, values)
            
        if node.right != None:
            self.traverse(node.right, values)
    
    def preorderTraversal(self, root):
        values = []
        self.traverse(root, values)
        return values


class InOrderSolution:
    def traverse(self, node, values):
        if node.left != None:
            self.traverse(node.left, values)

        values.append(node.val)

        if node.right != None:
            self.traverse(node.right, values)
    
    def inOrderTraversal(self, root):
        values = []
        
        if root:
            self.traverse(root, values)

        return values

class PostOrderSolution:
    def traverse(self, node, values):
        
        if node.left != None:
            self.traverse(node.left, values)
            
        if node.right != None:
            self.traverse(node.right, values)
            
        values.append(node.val)
        
    
    def postorderTraversal(self, root):
        values = []
        
        if root:
            self.traverse(root, values)
            
        return values
        

pre_order = PreOrderSolution()
in_order = InOrderSolution()
post_order = PostOrderSolution()

print(pre_order.preorderTraversal(root))    
print(in_order.inOrderTraversal(root))
print(post_order.postorderTraversal(root))