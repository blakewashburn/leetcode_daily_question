"""
Title:
1171. Remove Zero Sum Consecutive Nodes from Linked List

Description:
	Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
	After doing so, return the head of the final linked list.  You may return any such answer.
	(Note that in the examples below, all sequences are serializations of ListNode objects.)

Examples:
	Input: head = [1,2,-3,3,1]
	Output: [3,1]
	Note: The answer [1,2,1] would also be accepted.

	Input: head = [1,2,3,-3,4]
	Output: [1,2,4]

	Input: head = [1,2,3,-3,-2]
	Output: [1]

Constrains:
	The given linked list will contain between 1 and 1000 nodes.
	Each node in the linked list has -1000 <= node.val <= 1000.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        # create a new heads so that we can handle when head is deleted easily
        front = ListNode(0, head)
        current = front
        prefix_sum = 0

        # dictionary that we will use to track prefix sum and the node that has said prefix sum
        prefix_sum_to_node = {0: front}

        # Calculate the prefix sum for each node and add to the hashmap
        # Duplicate prefix sum values will be deleted
        while current:
            prefix_sum += current.val
            prefix_sum_to_node[prefix_sum] = current
            current = current.next

        # Reset prefix sum and current
        prefix_sum = 0
        current = front

        # Delete zero sum consecutive sequences 
        # by setting node before sequence to node after
        while current:
            prefix_sum += current.val
            current.next = prefix_sum_to_node[prefix_sum].next
            current = current.next

        # return the newest head by removing out head replacement
        return front.next



if __name__ == "__main__":
	sol = Solution()





	print(sol)