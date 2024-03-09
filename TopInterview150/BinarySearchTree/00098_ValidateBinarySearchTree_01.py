from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST_1(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= low or val >= high:
                return False
            if not dfs(node.right, val, high):
                return False
            if not dfs(node.left, low, val):
                return False
            return True

        return dfs(root)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            val = node.val
            if val <= low or val >= high:
                return False
            if node.left:
                if not dfs(node.left, low, val):
                    return False
            if node.right:
                if not dfs(node.right, val, high):
                    return False

            return True

        return dfs(root)


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution().isValidBST(root))

    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))  # 5,1,4,null,null,3,6
    print(Solution().isValidBST(root))