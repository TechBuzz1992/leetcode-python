class Node(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution(object):
    def addLists(self,l1,l2):
        carry = 0
        head = curr = Node(0)
        while l1 or l2:
            val = carry
            if l1:
                val+=l1.val
                l1 = l1.next
            if l2:
                val+=l2.val
                l2 = l2.next
            curr.next = Node(val%10)
            curr = curr.next
            carry = val/10
            if carry >0:
                curr.next = Node(carry)
            return head.next
            