# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return 
        if len(inorder) == 0: return
        root = TreeNode(preorder[0])

        split = inorder.index(root.val)

        left = inorder[:split]
        right = inorder[split+1:]
 

        root.left = self.buildTree(preorder[1:split+1], left)
        root.right = self.buildTree(preorder[split + 1:], right)

        return root
    

    


         