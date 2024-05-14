"""
Title: 
1026. Maximum Difference Between Node and Ancestor

Description: 
    Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
    A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.

Example:
    Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
    Output: 7
    Explanation: We have various ancestor-node differences, some of which are given below :
    |8 - 3| = 5
    |3 - 7| = 4
    |8 - 1| = 7
    |10 - 13| = 3
    Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

    Input: root = [1,null,2,null,0,3]
    Output: 3

Constraints:
    The number of nodes in the tree is in the range [2, 5000].
    0 <= Node.val <= 10^5

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        # pushing the nodeent node, the highest value, and the lowest value onto the queue
        queue = [(root, root.val, root.val)]

        # loop over queue
        while queue:
            node, highest, lowest = queue.pop(0)

            # calculate the new differences and check for new maximum difference
            ans = max(ans, node.val - lowest, highest - node.val)

            # if there is a left side, add that node with the highest value set at the node val or the highest value from before and set the lowest with either node value or the lowest from before
            if node.left:
                queue.append((node.left, max(node.val, highest), min(node.val, lowest)))
            if node.right:
                queue.append((node.right, max(node.val, highest), min(node.val, lowest)))

        return ans


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
