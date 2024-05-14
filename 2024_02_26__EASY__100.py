"""
Title: 
100. Same Tree

Description: 
  Given the roots of two binary trees p and q, write a function to check if they are the same or not.
  Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example:
  Input: p = [1,2,3], q = [1,2,3]
  Output: true

  Input: p = [1,2], q = [1,null,2]
  Output: false

  Input: p = [1,2,1], q = [1,1,2]
  Output: false

Constraints:
  The number of nodes in both trees is in the range [0, 100].
  -10^4 <= Node.val <= 10^4

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def dfs(p, q):
            
            # return True if both p and q are null
            if not p and not q: 
                return True

            # return False if only one is null
            elif not p or not q:
                return False
                
            # return false if their values are not equil
            if p.val != q.val:
                return False

            if dfs(p.left, q.left) and dfs(p.right, q.right):
                return True
            return False

        return dfs(p, q)
        

if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
