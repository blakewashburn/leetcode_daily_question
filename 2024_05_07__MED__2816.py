"""
Title:
2816. Double a Number Represented as a Linked List

Description:
    You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
    Return the head of the linked list after doubling it.

Examples:
    Input: head = [1,8,9]
    Output: [3,7,8]
    Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

    Input: head = [9,9,9]
    Output: [1,9,9,8]
    Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

Constrains:
    The number of nodes in the list is in the range [1, 10^4]
    0 <= Node.val <= 9
    The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def doubleIt(self, head):

        # create stack of nodes in list
        stack = []
        node = head
        while node: 
            stack.append(node)
            node = node.next
        
        # Loop over nodes in reverse order by poping from the top of the stack
        carry = 0
        while stack:

            # calculate double of value
            node = stack.pop(-1)
            new_val = int(node.val * 2) + carry

            # assign new value and determine next carry
            node.val = int(new_val % 10)
            carry = int((new_val - (new_val % 10)) / 10)
        
        # check for a remaining carry
        if carry > 0:
            head = ListNode(val=carry, next=head)

        return head



if __name__ == "__main__":
	sol = Solution()





	print(sol)