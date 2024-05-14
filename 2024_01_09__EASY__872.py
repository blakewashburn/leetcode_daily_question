"""
Title: 
    872. Leaf-Similar Trees

Description: 
    Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
    For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
    Two binary trees are considered leaf-similar if their leaf value sequence is the same.
    Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example:
    Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
    Output: true
    Input: root1 = [1,2,3], root2 = [1,3,2]
    Output: false

Constraints:
    The number of nodes in each tree will be in the range [1, 200].
    Both of the given trees will have values in the range [0, 200].

"""

from itertools import zip_longest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def leafSimilar(self, root1, root2) -> bool:

        # Depth first search from left to right, but use generators so we compare leaves as soon as they are found

        def dfs(root):
            # print(f'into dfs: \n\t root: {root}')
            
            # check if we are at a leaf 
            if root.left is None and root.right is None:
                yield root.val

            # when we are not in a leaf, then dfs on children
            else:
                if root.left:
                    yield from dfs(root.left)
                if root.right:
                    yield from dfs(root.right)
        
        sentenal = object()

        # loop over generators
        for val_1, val_2 in zip_longest(dfs(root1), dfs(root2), fillvalue=sentenal):

            # if leaves are not the same, we fail
            if val_1 != val_2:
                return False

            # if one tree is longer than the other, we fail
            if val_1 is sentenal or val_2 is sentenal:
                return False
        
        return True


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
