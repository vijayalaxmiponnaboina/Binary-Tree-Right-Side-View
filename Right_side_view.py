# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        q=deque()
        res=[]
        q.append(root)
        while len(q):
            l=len(q)
            level=[]
            for i in range(l):
                f=q.popleft()
                level.append(f.val)
                if f.left:
                    q.append(f.left)
                if f.right:
                    q.append(f.right)
            res.append(level[-1])
        return res