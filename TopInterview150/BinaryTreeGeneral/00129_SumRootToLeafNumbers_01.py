from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers_solution1(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path=""):
            if not node:
                return int(path)
            elif not node.left and not node.right:
                path += str(node.val)
                return int(path)
            
            path += str(node.val)
            left_sum, right_sum = 0, 0
            if node.left:
                left_sum = dfs(node.left, path)
            if node.right:
                right_sum = dfs(node.right, path)

            # left_sum = dfs(node.left, path)
            # right_sum = dfs(node.right, path)
            
            return left_sum + right_sum

        total = dfs(root, "")
        return total


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            if not node:
                return 0
            
            total = total * 10 + node.val
            if not node.left and not node.right:
                return total
            
            return dfs(node.left, total) + dfs(node.right, total)

        return dfs(root, 0)


if __name__ == '__main__':
    solution = Solution()

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    expected = 25
    assert solution.sumNumbers(root) == expected

    root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
    expected = 1026
    assert solution.sumNumbers(root) == expected

    root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    expected = 137
    assert solution.sumNumbers(root) == expected
