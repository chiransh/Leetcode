# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes_left=[]
        nodes_right=[]
        nodes_left.append(root)
        nodes_right.append(root)
        while True:
            node_left=nodes_left.pop()
            node_right=nodes_right.pop()
            if node_left!=node_right:
                return False
            if node_left.right is not None: 
                nodes_left.append(node_left.right) 
            elif node_left.left is not None: 
                nodes_left.append(node_left.left) 
            elif node_right.left is not None: 
                nodes_right.append(node_right.left) 
            elif node_right.right is not None: 
                nodes_right.append(node_right.right)
            else:
                return False
        return True

        
s=Solution()
print(s.isSymmetric([1,2,2,3,4,4,3]))