"""
Title: 
2385. Amount of Time for Binary Tree to Be Infected

Description: 
    You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
    Each minute, a node becomes infected if:
    - The node is currently uninfected.
    - The node is adjacent to an infected node.
    Return the number of minutes needed for the entire tree to be infected.

Example:
    Input: root = [1,5,3,null,4,10,6,9,2], start = 3
    Output: 4
    Explanation: The following nodes are infected during:
    - Minute 0: Node 3
    - Minute 1: Nodes 1, 10 and 6
    - Minute 2: Node 5
    - Minute 3: Node 4
    - Minute 4: Nodes 9 and 2
    It takes 4 minutes for the whole tree to be infected so we return 4.

    Input: root = [1], start = 1
    Output: 0
    Explanation: At minute 0, the only node in the tree is infected so we return 0.


Constraints:
    The number of nodes in the tree is in the range [1, 105].
    1 <= Node.val <= 105
    Each node has a unique value.
    A node with a value of start exists in the tree

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Node: 
    def __init__(self, parent=None, val=0, left=None, right=None):
        self.parent = parent
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, target_node=None):
        self.target_node = target_node

    # def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
    def amountOfTime(self, root, start: int) -> int:
         
        # copies the tree
        def copy_node(original_node, new_node, parent=None):
            new_node.val = original_node.val
            new_node.parent = parent

            # copy the remainder of the tree to the left
            if original_node.left:
                new_node.left = copy_node(original_node.left, Node(), new_node)
            
            # copy the remainder of the tree to the right
            if original_node.right:
                new_node.right = copy_node(original_node.right, Node(), new_node)

            # if we happen to be at where the infection starts, save that address
            if new_node.val == start:
                self.target_node = new_node
            return new_node
        
        # copy the tree into Node objects so that we track the parent
        root2 = copy_node(original_node=root, new_node=Node())
        queue = [(self.target_node, 0)]
        ans = 0
        seen_set = set()

        # now count the minutes until tree infected using BFS
        while queue:
            (node, distance_counter) = queue.pop(0)

            # check if we have visited this node before
            if node.val not in seen_set:
                seen_set.add(node.val)
                ans = max(ans, distance_counter)

                # add adjacent nodes to BFS queue
                if node.parent:
                    queue.append((node.parent, distance_counter + 1))
                if node.left:
                    queue.append((node.left, distance_counter + 1))
                if node.right:
                    queue.append((node.right, distance_counter + 1))
        
        return ans
            


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
