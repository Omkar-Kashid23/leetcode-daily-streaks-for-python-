# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)

        def dfs(node, level):
            if not node:return

            level_sum[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)
        max_sum = float('-inf')
        result_level = 0
        for level in sorted(level_sum):
            if level_sum[level]>max_sum:
                max_sum = level_sum[level]
                result_level = level
        return result_level
