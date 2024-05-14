"""
Title:
623. Add One Row to Tree

Description:
	Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.
	Note that the root node is at depth 1.
	The adding rule is:
		Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
		cur's original left subtree should be the left subtree of the new left subtree root.
		cur's original right subtree should be the right subtree of the new right subtree root.
		If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Examples:
	Input: root = [4,2,6,3,1,5], val = 1, depth = 2
	Output: [4,1,1,2,null,null,6,3,1,5]

	Input: root = [4,2,null,3,1], val = 1, depth = 3
	Output: [4,2,null,1,1,3,null,null,1]


Constrains:
	The number of nodes in the tree is in the range [1, 10^4].
	The depth of the tree is in the range [1, 10^4].
	-100 <= Node.val <= 100
	-10^5 <= val <= 10^5
	1 <= depth <= the depth of tree + 1

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:

        # BFS method

        # check for empty root
        if depth == 1:
            return TreeNode(val=val, left=root)

        # Loop through nodes via BFS
        queue = [(root, 1)]
        while queue: 

            # grap front node
            tup = queue.pop(0)
            cur_node, cur_node_depth = tup[0], tup[1]

            # check that we have gotten past the target depth
            if cur_node_depth >= depth: 
                break
                    
            # check that we are at the target depth
            if cur_node_depth == depth - 1:

                # insert nodes
                cur_node.left = TreeNode(val=val, left=cur_node.left)
                cur_node.right = TreeNode(val=val, right=cur_node.right)
                
            # Add nodes to the queue  
            if cur_node.left:
                queue.append((cur_node.left, cur_node_depth + 1))
            if cur_node.right:
                queue.append((cur_node.right, cur_node_depth + 1))
        
        return root



if __name__ == "__main__":
	sol = Solution()





	print(sol)