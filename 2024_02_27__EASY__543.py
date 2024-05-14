"""
Title: 
543. Diameter of Binary Tree

Description: 
  Given the root of a binary tree, return the length of the diameter of the tree.
  The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
  The length of a path between two nodes is represented by the number of edges between them.

Example:
  Input: root = [1,2,3,4,5]
  Output: 3
  Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

  Input: root = [1,2]
  Output: 1

Constraints:
  The number of nodes in the tree is in the range [1, 104].
  -100 <= Node.val <= 100

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self): 
        self.ans = 0

    # calculates the depth of the left and right nodes and then returns the larger one
    def dfs(self, node, max_depth):

        # check if we have reached the bottom
        if not node:
            return -1
        
        # find the deepest path on both sides
        max_depth_left = self.dfs(node=node.left, max_depth=max_depth) + 1
        max_depth_right = self.dfs(node=node.right, max_depth=max_depth) + 1

        # check if this node should be the root of the diameter
        self.ans = max(self.ans, max_depth_left + max_depth_right)

        # return the deepest path available
        return max(max_depth_left, max_depth_right)
        

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        # find diameter
        self.dfs(node=root, max_depth=0)

        return self.ans
        


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
