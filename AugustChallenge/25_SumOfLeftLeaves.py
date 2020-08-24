'''
Find the sum of all left leaves in a given binary tree.

Example:
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum_left_leaves = 0
        if root is None:
            return 0
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                sum_left_leaves += root.left.val
            else:
                sum_left_leaves += self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            sum_left_leaves += self.sumOfLeftLeaves(root.right)
        return sum_left_leaves


t15 = TreeNode(15)
t07 = TreeNode(7)
t20 = TreeNode(20, t15, t07)
t09 = TreeNode(9)
tree_root = TreeNode(3, t09, t20)

solution = Solution()
print(solution.sumOfLeftLeaves(tree_root))
