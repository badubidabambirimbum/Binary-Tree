class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node = TreeNode(2, TreeNode(1), TreeNode(3))

print(node.val)
print(node.left.val)
print(node.right.val)