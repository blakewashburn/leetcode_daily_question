"""
Title:
129. Sum Root to Leaf Numbers

Description:
	You are given the root of a binary tree containing digits from 0 to 9 only.
	Each root-to-leaf path in the tree represents a number.
		For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
	Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
	A leaf node is a node with no children.

Examples:
	Input: root = [1,2,3]
	Output: 25
	Explanation:
	The root-to-leaf path 1->2 represents the number 12.
	The root-to-leaf path 1->3 represents the number 13.
	Therefore, sum = 12 + 13 = 25.

	Input: root = [4,9,0,5,1]
	Output: 1026
	Explanation:
	The root-to-leaf path 4->9->5 represents the number 495.
	The root-to-leaf path 4->9->1 represents the number 491.
	The root-to-leaf path 4->0 represents the number 40.
	Therefore, sum = 495 + 491 + 40 = 1026.

Constrains:
	The number of nodes in the tree is in the range [1, 1000].
	0 <= Node.val <= 9
	The depth of the tree will not exceed 10.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root) -> int:

        # BFS keeping a list of strings

        ans = 0
        queue = [(root, "")]

        # BFS over tree
        while queue:
            
            # grab front node and calculate root-to-leaf path of front node
            tup = queue.pop(0)
            node = tup[0]
            val_with_node_val = tup[1] + str(node.val)

            # check for leaf and add root-to-leaf path if necessary
            if not node.left and not node.right:
                ans += int(val_with_node_val)

            # Add children to queue if they exist 
            else:
                if node.left:
                    queue.append((node.left, val_with_node_val))
                if node.right:
                    queue.append((node.right, val_with_node_val))
        
        return ans

        



if __name__ == "__main__":
	sol = Solution()


	root = [1,2,3]			# -> 25
	root = [4,9,0,5,1]			# -> 1026


	print(sol.sumNumbers(root=root))