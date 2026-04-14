# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp,curr = None ,head
        while (curr!=None):
            nxt = curr.next #temporary variable hai to store the next value
            curr.next = temp # reverse order starting with None temp = previous value of the list
            temp = curr
            curr = nxt
        return temp


        