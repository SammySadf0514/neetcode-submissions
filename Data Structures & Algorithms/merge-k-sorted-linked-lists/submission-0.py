# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for head in lists:
            current = head

            while current:
                res.append(current.val)
                current = current.next

        res.sort()
        dummy = ListNode()
        current = dummy

        for x in res:
            current.next = ListNode(x)
            current = current.next

        return dummy.next