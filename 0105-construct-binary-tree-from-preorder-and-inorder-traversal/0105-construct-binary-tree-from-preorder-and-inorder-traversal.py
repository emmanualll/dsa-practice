# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorderIdx = {v : i for i,v in enumerate(inorder)}
        preIdx = 0

        def helper(l, r):
            nonlocal preIdx

            if l > r:
                return None
            
            root = TreeNode(preorder[preIdx])
            preIdx += 1

            idx = inorderIdx[root.val]

            root.left = helper(l, idx - 1)
            root.right = helper(idx+1, r)
            return root
        
        return helper(0, len(inorder) - 1)
        