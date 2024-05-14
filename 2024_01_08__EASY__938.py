"""
Title: 
938. Range Sum of BST

Description: 
    Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example:
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23
    Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        
        ans = 0
        queue = [root]

        # BFS
        while queue:
            node = queue.pop(0)

            # when node.val is between desired range
            if low <= node.val <= high:
                ans += node.val
                
                # add both children to queue for checking
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # when node.val is below desired range
            elif node.val <= low:

                # we only want to check the righ child
                if node.right:
                    queue.append(node.right)

            # when node.val is above desired range
            elif high <= node.val:

                # we only want to check the left child
                if node.left:
                    queue.append(node.left)

        return ans


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
