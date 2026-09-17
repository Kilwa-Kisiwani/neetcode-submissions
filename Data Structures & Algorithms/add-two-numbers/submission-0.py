# Definition for singly-linked list.
# class ListNode:
from os import error
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr = None
        carry = 0

        def getDigit(l1: Optional[ListNode], l2:Optional[ListNode], carry: int) ->tuple[Optional[ListNode], int]:
            if l1 and l2:
                digit = l1.val + l2.val
            else:
                if l1:
                    digit = l1.val
                elif l2:
                    digit = l2.val
                else:
                    return None, 0
            if carry == 1:
                carry = 0
                digit += 1
            if digit >= 10:
                carry = 1
                digit %= 10
            digit = ListNode(digit)
            return digit, carry

        while l1 and l2:
            digit, carry = getDigit(l1, l2, carry)
            l1 = l1.next
            l2 = l2.next
            if not res or not curr:
                res = digit
                curr = res
            else:
                curr.next = digit
                curr = curr.next
        if l1:
            while l1:
                digit, carry = getDigit(l1, None, carry)
                l1 = l1.next
                if not res or not curr:
                    res = digit
                    curr = res
                else:
                    curr.next = digit
                    curr = curr.next
        if l2:
            while l2:
                digit, carry = getDigit(l2, None, carry)
                l2 = l2.next
                if not res or not curr:
                    res = digit
                    curr = res
                else:
                    curr.next = digit
                    curr = curr.next
        if carry == 1:
            tmp = ListNode(1)
            if curr:
                curr.next = tmp
            else:
                error("Not possible")
        
        return res
            