# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # cody's solution

        queue = [[root]]

        i = 0
        while i < len(queue):
            next_queue = []

            for node in queue[i]:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                
            if next_queue:
                queue.append(next_queue)
            
            i += 1
        
        ans = [[node.val for node in level] for level in queue]
        return ans