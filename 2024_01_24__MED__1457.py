"""
Title: 
1457. Pseudo-Palindromic Paths in a Binary Tree

Description: 
    Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
    Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

Example:
    Input: root = [2,3,1,3,1,null,1]
    Output: 2 
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).

    Input: root = [2,1,1,1,3,null,null,null,null,null,1]
    Output: 1 
    Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).

    Input: root = [9]
    Output: 1

Constraints:
    The number of nodes in the tree is in the range [1, 10^5].
    1 <= Node.val <= 9

"""

from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def isPalindrome(self, freq_dict:dict) -> bool:
        seen_an_odd_freq = False    # tracks how many odd frequencies we have seen

        # loop over values in dictionary
        for key in freq_dict.keys():
            
            # check if num occurs an odd number of times
            if freq_dict[key] % 2 != 0:

                # if this is the second odd frequency we have, then cannot be a palendrome
                if seen_an_odd_freq:
                    return False
                else:
                    seen_an_odd_freq = True
        
        return True

    def dfs(self, node, freq_dict:dict) -> None:
        freq_dict[node.val] += 1

        # check for leaf
        if not node.left and not node.right:

            # check for palindrome
            if self.isPalindrome(freq_dict):
                self.ans += 1

        # not a leaf
        else:

            # recursively call dfs
            if node.left:
                self.dfs(node=node.left, freq_dict=freq_dict.copy())
            if node.right:
                self.dfs(node=node.right, freq_dict=freq_dict.copy())
            # dictionaries must be copied so that they dont overwrite each other
            

    def pseudoPalindromicPaths(self, root) -> int:
        self.dfs(node=root, freq_dict=defaultdict(int))
        return self.ans
        


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
