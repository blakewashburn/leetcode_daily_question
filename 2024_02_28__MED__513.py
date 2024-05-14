"""
Title: 
513. Find Bottom Left Tree Value

Description: 
    Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example:
    Input: root = [2,1,3]
    Output: 1

    Input: root = [1,2,3,4,null,5,6,null,null,7]
    Output: 7

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    -2^31 <= Node.val <= 2^31 - 1

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        # BFS and we take the first value at the deepest level
        # first value will always be left most if we go left to right across tree

        queue = [(root, 0)]
        ans = (root.val, 0)

        while queue:
            root_and_level = queue.pop(0)

            # check if we have reached a new, deeper level
            # if so, update the answer
            if root_and_level[1] > ans[1]:
                ans = (root_and_level[0].val, root_and_level[1])
            
            # add children to queue
            if root_and_level[0].left:
                queue.append((root_and_level[0].left, root_and_level[1] + 1))
            if root_and_level[0].right:
                queue.append((root_and_level[0].right, root_and_level[1] + 1))
        
        return ans[0]


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
