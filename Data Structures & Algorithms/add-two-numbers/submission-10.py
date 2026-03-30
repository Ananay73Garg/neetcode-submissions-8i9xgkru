# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n = 1
        x = 0
        tx = l1
        ty = l2
        t1,t2 = tx,ty
        while t1 or t2:
            if t1 and not t2:
                x += (t1.val)*n
                n *=10
                t1 = t1.next
            elif t2 and not t1:
                x += (t2.val)*n
                n *=10
                t2 = t2.next
            else:
                x += (t1.val + t2.val)*n
                n *=10
                t1,t2 = t1.next,t2.next
        
        y = ListNode(0)
        cur = y

        for d in str(x)[::-1]:
            cur.next = ListNode(int(d))
            cur = cur.next

        return y.next

        
