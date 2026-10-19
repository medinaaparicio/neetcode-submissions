# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key == root.val:
            # o no tienes hijos
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = self.minValNode(root.right) # in order successor, want to mantain the BST
                # switch their values 
                root.val = minNode.val
                # and reorg
                root.right = self.deleteNode(root.right, minNode.val)
        return root
        # # if we never found the key?
        # else: return root

            
        