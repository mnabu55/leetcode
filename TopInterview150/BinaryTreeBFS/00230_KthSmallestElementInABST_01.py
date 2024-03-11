from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, values):
            if not node:
                return
            inorder(node.left, values)
            values.append(node.val)
            inorder(node.right, values)        

        values = []
        inorder(root, values)
        return values[k - 1]


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(solution.kthSmallest(root, 1))
