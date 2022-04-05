
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



class SymmetrySolution:
    def leftSideSymmetry(self, node, leftValues):
        if node == None: 
            leftValues.append(None)
            return
        
        leftValues.append(node.val)
        
        self.leftSideSymmetry(node.left, leftValues)
        self.leftSideSymmetry(node.right, leftValues)
            
        if node.left == None and node.right == None:
            return
        
        
    def rightSideSymmetry(self, node, rightValues):
        if node == None: 
            rightValues.append(None)
            return
        
        rightValues.append(node.val)
    
        self.rightSideSymmetry(node.right, rightValues)
        self.rightSideSymmetry(node.left, rightValues)
    
        if node.left == None and node.right == None:
            return
        
    
    def isSymmetric(self, root):
        
        leftValues = []
        rightValues = []
        
        self.leftSideSymmetry(root, leftValues)
        self.rightSideSymmetry(root, rightValues)
        
        print(leftValues)
        print(rightValues)

        if leftValues == rightValues:
            return True
        else:
            return False




symmetry = SymmetrySolution()

root = TreeNode(1, TreeNode(2, None, TreeNode(3)),TreeNode(2,None, TreeNode(3)))

print(symmetry.isSymmetric(root))
    
        

# pre_order = PreOrderSolution()
# in_order = InOrderSolution()
# post_order = PostOrderSolution()

# print(pre_order.preorderTraversal(root))    
# print(in_order.inOrderTraversal(root))
# print(post_order.postorderTraversal(root))