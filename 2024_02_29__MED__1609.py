"""
Title: 
1609. Even Odd Tree

Description: 
    A binary tree is named Even-Odd if it meets the following conditions:
        The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
        For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
        For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
    Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.

Example:
    Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
    Output: true
    Explanation: The node values on each level are:
    Level 0: [1]
    Level 1: [10,4]
    Level 2: [3,7,9]
    Level 3: [12,8,6,2]
    Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.

    Input: root = [5,4,2,3,3,7]
    Output: false
    Explanation: The node values on each level are:
    Level 0: [5]
    Level 1: [4,2]
    Level 2: [3,3,7]
    Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.

    Input: root = [5,9,1,3,5,7]
    Output: false
    Explanation: Node values in the level 1 should be even integers.

Constraints:
    The number of nodes in the tree is in the range [1, 105].
    1 <= Node.val <= 106

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:

        # BFS and check condition of all nodes at a level when we change levels

        def even_odd_condition_check(list_of_nodes: list[TreeNode], level: int) -> bool:
            
            # determine if we are checking for even level or odd level conditions
            if level % 2 == 0:
                
                # check even condition
                prev_val = -float('inf')
                for node in list_of_nodes:

                    # return false if node.val is even or smaller than previous node.val
                    if node.val % 2 == 0 or node.val <= prev_val:
                        return False
                    print(f'prev_val: {prev_val} and node.val: {node.val}')
                    prev_val = node.val
            
            else:
                # check odd condition
                prev_val = float('inf')
                for node in list_of_nodes:

                    # return false if node.val is odd or larger than previous node.val
                    if node.val % 2 != 0 or node.val >= prev_val:
                        return False
                    prev_val = node.val
            
            return True
        
        queue = [(root, 0)]
        nodes_at_a_level = []
        current_level = 0
        while queue:

            node_and_level = queue.pop(0)

            # check if we have reached a new level
            if nodes_at_a_level:
                if node_and_level[1] != current_level:
                    
                    # we are at a new level, so check conditions of prev level
                    if not even_odd_condition_check(nodes_at_a_level, current_level):
                        return False
                    nodes_at_a_level = []
                    current_level += 1
            
            # add the current node to our level list
            nodes_at_a_level.append(node_and_level[0])
            
            # add children to queue
            if node_and_level[0].left:
                queue.append((node_and_level[0].left, node_and_level[1] + 1))
            if node_and_level[0].right:
                queue.append((node_and_level[0].right, node_and_level[1] + 1))

        # check condition for last level
        if not even_odd_condition_check(nodes_at_a_level, current_level):
            return False
        
        return True

        



        
        


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
