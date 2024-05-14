"""
Title: 
876. Middle of the Linked List

Description: 
  Given the head of a singly linked list, return the middle node of the linked list.
  If there are two middle nodes, return the second middle node.

Example:
  Input: head = [1,2,3,4,5]
  Output: [3,4,5]
  Explanation: The middle node of the list is node

  Input: head = [1,2,3,4,5,6]
  Output: [4,5,6]
  Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
  The number of nodes in the list is in the range [1, 100].
  1 <= Node.val <= 100

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        # 2 pointer method
        slow_pointer, fast_pointer = head, head.next

        # loop until we get to last or beyond last node
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        # if fast pointer is at last node, then we have an even number of nodes
        # meaning we need to return the second middle node
        if fast_pointer:
            return slow_pointer.next

        #  if fast is beyond last node, then slow is at middle
        return slow_pointer
        
        


if __name__ == "__main__":
    sol = Solution()
    


    print(sol)
