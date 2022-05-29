# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        itr = head
        length=1
        while (itr.next is not None):
            length = length+1
            itr = itr.next
        rval = 0
        itr = head
        length = length-1
        while (itr.next is not None):
            rval = rval + itr.val*pow(2,length)
            length=length-1
            itr = itr.next
        return rval +itr.val
        