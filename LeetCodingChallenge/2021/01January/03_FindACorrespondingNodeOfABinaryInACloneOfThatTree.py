'''
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

Follow up: Solve the problem if repeated values on the tree are allowed.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    clonedTarget = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.dfs(cloned, target.val)
        return self.clonedTarget

    def dfs(self, root: TreeNode, val: int):
        if root == None:
            return
        self.dfs(root.left, val)
        if root.val == val:
            self.clonedTarget = root
        self.dfs(root.right, val)
