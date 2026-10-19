# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthHelper(self, root: Optional[TreeNode], k: int, ordered: List[TreeNode]):
        if not root: return 

        self.kthHelper(root.left, k, ordered)
        ordered.append(root.val)
        self.kthHelper(root.right, k, ordered)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered = []
        self.kthHelper(root, k, ordered)
        return ordered[k-1]
