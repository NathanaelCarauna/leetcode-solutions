# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result = []
        result1 = []
        def order(root, result):
            if not root:
                result.append(None)
                return
            order(root.left, result)
            order(root.right, result)
            result.append(root.val)     
        order(p, result)   
        order(q, result1)   
        return result == result1